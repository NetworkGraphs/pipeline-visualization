import time
import runner as run

def fetch():
    print("- fetching file")
    time.sleep(0.1)
    my_data = {
        "hello":"world"
    }
    run.set_artifact(my_data,"fetch/content.json")
    return

def calculate():
    print("- hello from calc2")
    new_data = run.get_artifact("content")
    time.sleep(0.3)
    print(new_data)
    run.set_artifact({"stats":5},"fetch/stats.json")
    return

def compute():
    print("- hellor from comp3")
    new_data = run.get_artifact("content")
    time.sleep(0.4)
    run.set_artifact({"result":6},"fetch/result.json")
    return

def build():
    print("- hi build4")
    stats = run.get_artifact("stats")
    result = run.get_artifact("result")
    time.sleep(0.5)
    run.set_artifact({"web":10},"fetch/website.json")
    return
