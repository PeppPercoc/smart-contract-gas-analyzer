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
    per_page=3
    max_pages=1 #20*50=1000 numero massimo richieste
    for page in range(1,max_pages+1):
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={per_page}&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Errore {response.status_code}: {response.text}")
            break
        repos.extend(response.json().get("items", []))
    return repos

def get_commit(full_name):
    print(full_name)

def main():
    star="10"
    language="Solidity"
    created="2019-01-01"
    archived="false"
    query="stars:>"+star+" language:"+language+" created:>"+created+" archived:"+archived
    repos=search_repository(query)
    fieldnames = repos[0].keys()
    with open("output/repos.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in repos:
            full_name=repo["full_name"]
            commit = get_commit(full_name)
            writer.writerow(repo)

if __name__ == "__main__":
    main()
