import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("Token GitHub non trovato! Controlla il file .env")

def main():
    print(GITHUB_TOKEN)

if __name__ == "__main__":
    main()
