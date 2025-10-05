# smart-contract-gas-analyzer
A Python tool for analyzing commits in smart contract repositories to study gas optimizations and code evolution.

## Requirements

- Docker and Docker Compose installed on your system  
- A GitHub Personal Access Token (Fine-grained PAT) with read access to public repositories

## Setup

1. Create a `.env` file in the project root with the following content:

   ```
   GITHUB_TOKEN=your_github_token_here
   ```

2. Create an output folder:

   ```bash
   mkdir -p output
   ```

## Run with Docker Compose

Simply build and run the container using:

```bash
docker compose up
```

If you make changes to the code and want to rebuild the image:

```bash
docker compose build --no-cache
```

This will:
- Build the image automatically if it does not exist  
- Load environment variables from `.env`  
- Mount the `output` directory to store the results  
- Run the analysis script inside the container  

## Output

After execution, the results will be saved in:

```
output/solidity_repositories.csv
```
