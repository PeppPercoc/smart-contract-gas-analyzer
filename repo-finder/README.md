# repo-finder

This module searches for public GitHub repositories containing Solidity smart contracts, collects relevant metadata (stars, forks, commits, etc.), and exports the results to a CSV file for further analysis.

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
