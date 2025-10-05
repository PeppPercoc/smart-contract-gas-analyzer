import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("Github Token not found! Check file .env")

def search_repository(query):
    repos=[]
    per_page=50
    max_pages=20 #20*50=1000 numero massimo richieste
    for page in range(1,max_pages+1):
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={per_page}&page={page}"
        print("l'url è ")
        print(url)


def main():
    print(GITHUB_TOKEN)
    star="10"
    language="Solidity"
    created="2019-01-01"
    archived="false"
    query="stars:>"+star+" language:"+language+" created:>"+created+" archived:"+archived
    repos=search_repository(query)

if __name__ == "__main__":
    main()
