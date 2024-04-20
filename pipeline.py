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
    print(new_data)
    return

def compute():
    print("- hellor from comp3")
    return

def build():
    print("- hi build4")
    return
