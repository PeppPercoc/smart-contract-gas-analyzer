import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("Github Token not found! Check file .env")

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def search_repository(query):
    repos=[]
    per_page=50
    max_pages=1 #20*50=1000 numero massimo richieste
    for page in range(1,max_pages+1):
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={per_page}&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Errore {response.status_code}: {response.text}")
            break
        repos.extend(response.json().get("items", []))
    return repos

def get_commits_count(full_name):
    url = f"https://api.github.com/repos/{full_name}/commits?per_page=1"
    response = requests.get(url, headers=HEADERS)
    link=response.headers.get("link",[])
    if link:
        pos = link.rfind("page=")
        if pos != -1:
            part = link[pos + 5:]
            end = part.find(">")
            if end != -1:
                last_page = part[:end]
                return int(last_page)
    return 0

def get_contributors_count(full_name):
    url = f"https://api.github.com/repos/{full_name}/contributors?per_page=1&anon=true"
    response = requests.get(url, headers=HEADERS)
    link=response.headers.get("link",[])
    if link:
        pos = link.rfind("page=")
        if pos != -1:
            part = link[pos + 5:]
            end = part.find(">")
            if end != -1:
                last_page = part[:end]
                return int(last_page)
    return 0

def main():
    star="9"
    language="Solidity"
    created="2019-01-01"
    archived="false"
    query="stars:>"+star+" language:"+language+" created:>"+created+" archived:"+archived
    repos=search_repository(query)
    fieldnames = list(repos[0].keys())+["commits_count"]+["contributors_count"]
    with open("output/repos.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in repos:
            full_name=repo["full_name"]
            commits = get_commits_count(full_name)
            contributors = get_contributors_count(full_name)
            if 50 < commits < 300 and contributors > 4:
                repo["commits_count"] = commits
                repo["contributors_count"]= contributors
                writer.writerow(repo)

if __name__ == "__main__":
    main()
