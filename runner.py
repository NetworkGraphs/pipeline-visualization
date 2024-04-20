import utils as utl
import importlib
from os.path import dirname,splitext,basename,join
import state
from datetime import datetime

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
    return

def get_artifact(id):
    if(id not in state.artifacts):
        raise ArtifactError(f"Artifact with ID '{id}' does not exist")
    artifact = state.artifacts[id]
    if(artifact["ext"] == ".json"):
        return utl.load_json(join("cache",artifact["filepath"]))
    return None

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

def run_pipeline(pipeline):
    state.value = 1
    for stage, jobs in pipeline.items():
        run_stage(stage, jobs)
    utl.save_json(state.artifacts,"cache/artifacts.json")
    utl.save_json(state.pipe,"cache/pipeline.json")
    

if __name__ == '__main__':
    manifest = utl.load_yaml("manifest.yaml")
    run_pipeline(manifest["pipeline"])
