# Smart Contract Gas Analyzer

A Python tool for analyzing commits in smart contract repositories to study gas optimizations and code evolution.

The system is divided into two main components, each contained in its own folder:

---

## 📁 Project Structure

### 1. `repo-finder/`
This module is responsible for **discovering Solidity repositories** on GitHub.  
It uses the GitHub API to search for public projects containing `.sol` files, collect metadata (stars, forks, last commit, etc.), and save the results into a CSV file for further analysis.

---

### 2. `commit-analyzer/`
This module performs a **commit-by-commit analysis** of repositories found by the first module.  
It can inspect changes to Solidity files, measure gas-related modifications, and prepare datasets for further study or visualization.
