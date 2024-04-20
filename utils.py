import json
import yaml
from os import makedirs
from os.path import dirname
from datetime import timedelta

def load_yaml(fileName):
    with open(fileName, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return

def load_json(fileName):
    return json.load(open(fileName,encoding='utf-8'))

def save_json(data,fileName):
    path = dirname(fileName)
    makedirs(path, exist_ok=True)
    jfile = open(fileName, "w")
    jfile.write(json.dumps(data, indent=4))
    jfile.close()
    return

def duration_text(duration: timedelta):
    # Ensure that the duration is non-negative
    if duration < timedelta(0):
        duration = -duration
    # Extract days, seconds, and microseconds from the timedelta object
    days = duration.days
    seconds = duration.seconds
    microseconds = duration.microseconds
    milliseconds = microseconds // 1000  # Convert microseconds to milliseconds

    # Calculate hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    # Build the duration text string
    text = ""
    if days > 0:
        text += f"{days} d "
    if hours > 0:
        text += f"{hours} h "
    if minutes > 0:
        text += f"{minutes} mn "
    if seconds > 0:
        text += f"{seconds} s "
    if milliseconds > 0:
        text += f"{milliseconds} ms "

    return text.strip()  # Remove any trailing space
