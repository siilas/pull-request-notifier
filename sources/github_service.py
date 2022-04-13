import os
import requests

repo_owner = os.getenv("REPO_OWNER", "")
repo_name = os.getenv("REPO_NAME", "")

url = "https://api.github.com/repos/{repo_owner}/{repo_name}/pulls?state=open"
headers = { "Accept": "application/vnd.github.v3+json" }

def get_open_pull_requests():
    print("Getting open pull requests...")
    
    if not repo_owner:
        raise Exception("The repository owner must be set in the enviroment variable: REPO_OWNER") 
    
    if not repo_name:
        raise Exception("The repository name must be set in the enviroment variable: REPO_NAME")
    
    return requests.get(url.format(repo_owner = repo_owner, repo_name = repo_name), headers = headers)
