import utils as utl
import importlib
from os.path import dirname,splitext,basename,join
import state
from datetime import datetime
import graph_utils as gutl
from containers import run

class ArtifactError(Exception):
    """Custom exception for artifact management errors."""
    pass

def log_job(stage_name, job_name,start):
    stop = datetime.now()
    state.pipe.append({
        "stage":stage_name,
        "job":job_name,
        "start":str(start),
        "stop":str(stop),
        "duration": str(stop-start),
        "duration_text": utl.duration_text(stop-start)
    })
    return

def set_artifact(data,filepath,type="generic"):
    id,ext = splitext(basename(filepath))
    if(id in state.artifacts):
        raise ArtifactError(f"Artifact with ID '{id}' already exists.")
    path = dirname(filepath)
    state.artifacts[id] = {
        "path":path,
        "ext":ext,
        "type":type,
        "filepath":filepath
    }
    abs_filepath = join("cache",filepath)
    if(ext == ".json"):
        utl.save_json(data,abs_filepath)
    gutl.add_edge({"label":state.job,"class":"job"},{"label":id,"class":"artifact"})
    return

def get_artifact(id):
    if(id not in state.artifacts):
        raise ArtifactError(f"Artifact with ID '{id}' does not exist")
    artifact = state.artifacts[id]
    gutl.add_edge({"label":id,"class":"artifact"},{"label":state.job,"class":"job"})
    if(artifact["ext"] == ".json"):
        return utl.load_json(join("cache",artifact["filepath"]))
    return None

def set_asset(data,filepath,type="generic"):
    filepath = join("assets",filepath)
    id,ext = splitext(basename(filepath))
    if(id in state.assets):
        raise ArtifactError(f"Asset with ID '{id}' already exists.")
    path = dirname(filepath)
    state.assets[id] = {
        "path":path,
        "ext":ext,
        "type":type,
        "filepath":filepath.replace("\\","/")
    }
    abs_filepath = join("cache",filepath)
    if(ext == ".json"):
        utl.save_json(data,abs_filepath)
    elif(ext == ".dot"):
        utl.save_text(data,abs_filepath)
    if(type == "graph"):
        utl.save_text(gutl.get_dot_graph(data),join("cache",path,f"{id}.dot"))
        run.graphviz(f"assets/{id}.dot")
    return

def run_stage(stage_name, jobs):
    print(f"Running stage: {stage_name}")
    state.stage = stage_name
    for job_name, job in jobs.items():
        module_name, function_name = job.split('#')
        state.job = job_name
        state.step = function_name
        module = importlib.import_module(module_name.replace('.py', ''))
        func = getattr(module, function_name)
        print(f"    Executing job: {job_name}")
        start = datetime.now()
        func()
        log_job(stage_name, job_name,start)

def run_post_build():
    set_asset(state.pipe,"pipeline.json")
    dep_graph = gutl.get_graph()
    set_asset(dep_graph,"dependencies.json",type="graph")
    timeline = generate_timeline(state.pipe)
    set_asset(timeline,"timeline.json")
    state.artifacts.update(state.assets)
    set_asset(state.artifacts,"artifacts.json")
    return

def run_pipeline(pipeline):
    state.value = 1
    for stage, jobs in pipeline.items():
        run_stage(stage, jobs)
    run_post_build()


def generate_timeline(pipe):
    items = []
    groups = []
    groups_names = []   #user to keep entries unique
    for item in pipe:
        if(item["stage"] not in groups_names):
            groups_names.append(item["stage"])
            groups.append({
                    "id":item["stage"],
                    "content":item["stage"]
                })
        items.append({
            "id":item["job"],
            "content":item["job"],
            "group":item["stage"],
            "start":item["start"],
            "end":item["stop"]
        })
    timeline = {
        "items":items,
        "groups":groups
    }
    return timeline

manifest = utl.load_yaml("manifest.yaml")
if __name__ == '__main__':
    run_pipeline(manifest["pipeline"])
