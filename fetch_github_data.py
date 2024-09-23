
import os
import requests
from git import Repo

def clone_repo(repo_url, clone_dir):
    if os.path.exists(clone_dir):
        print(f"Directory {clone_dir} already exists. Pulling latest changes.")
        repo = Repo(clone_dir)
        repo.remotes.origin.pull()
    else:
        print(f"Cloning repository {repo_url} into {clone_dir}.")
        Repo.clone_from(repo_url, clone_dir)

def fetch_github_data():
    repo_url = "https://github.com/John433-max/Infinity.git"
    clone_dir = "cloned_repo"
    clone_repo(repo_url, clone_dir)
    # Process the cloned repository as needed

if __name__ == '__main__':
    fetch_github_data()
