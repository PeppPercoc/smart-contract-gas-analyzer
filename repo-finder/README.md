# Smart-contract-gas-analyzer
A Python tool for analyzing commits in smart contract repositories to study gas optimizations and code evolution.

## Requirements

- Docker and Docker Compose installed on your system
- A GitHub Personal Access Token (Fine-grained PAT) with read access to public repositories

## Setup

1. Create a `.env` file in the project root with the following content:

   ```
   GITHUB_TOKEN=your_github_token_here
   ```

> Note: The `.env` file should not contain real credentials if you are sharing the project. Use `.env.example` as a template.

## Run with Docker Compose

Simply build and run the container using:

```bash
docker compose run --rm analyzer
```

If you make changes to the code and want to reconstruct the image you must delete the existing one and recreate it

## Output

After execution, the results will be saved in:

```
output/solidity_repositories.csv
```

## Cross-platform compatibility

- This setup works on **Linux, macOS, and Windows**.
- On Windows, ensure the project folder is shared with Docker Desktop so the `output` volume is mounted correctly.
