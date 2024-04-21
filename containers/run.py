import sys
import subprocess
import os

def graphviz(filename):
    os.chdir(docker_compose_dir)
    command_line = f"docker compose run --rm graphviz -Tsvg {filename} -o {filename}.svg"
    subprocess.run(command_line.split(" "))
    os.chdir(original_dir)
    return

def run(command):
    # Path to the directory containing docker-compose.yml
    if(command == "graphviz"):
        filename = sys.argv[2]
        graphviz(filename)
    elif(command == "server"):
        os.chdir(docker_compose_dir)
        subprocess.run("docker compose up apache", shell=True, check=True)
        os.chdir(original_dir)

original_dir = os.getcwd()
docker_compose_dir = os.path.join(os.path.dirname(__file__))

if __name__ == '__main__':
    # Default command if no argument is provided
    command = "build"
    # Check if an argument is provided and use it as the command
    if len(sys.argv) > 1:
        command = sys.argv[1]
    run(command)
