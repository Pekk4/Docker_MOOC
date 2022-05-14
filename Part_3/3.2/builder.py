import sys
import subprocess
import docker
from os import getenv


user = getenv("DHUB_USER")
client = docker.from_env()


def parse_repository_name(url):
    url_splitted = url.split("/")
    repository_name = url_splitted[-1].split(".git")[0]

    return repository_name

def clone_repository(url):
    subprocess.run(["git", "clone", url, "build/"])

def build_container(name):
    global tag
    tag = user + "/" + name

    print("Building container...")

    client.images.build(path="build/", tag=tag)

    print("Container built!")

    subprocess.run(["rm", "-rf", "build/"])

def login_docker_hub():
    token = getenv("DHUB_TOKEN")

    print("Logging into Docker Hub...")

    client.login(user, token)

def push_container():
    print("Pushing container to Docker Hub...")

    client.api.push(tag)

    print("Container pushed succesfully!")

def main():
    if len(sys.argv) <= 1:
        sys.exit("Repository is required! Quitting...")
    
    url = sys.argv[1]

    repository_name = parse_repository_name(url)

    clone_repository(url)
    build_container(repository_name)
    login_docker_hub()
    push_container()


if __name__ == "__main__":
    main()
