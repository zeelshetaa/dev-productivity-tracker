# Developer Productivity Tracker

A Python tool that analyzes Git repositories to measure developer productivity.

It extracts commit statistics, code changes, and repository activity using Git CLI commands.

## Features

- Track total commits
- Count lines added and removed
- Detect number of modified files
- Generate productivity report

## Tech Stack

Python  
Git CLI

## Project Structure

dev-productivity-tracker

main.py  
git_analyzer.py  
report_generator.py  
utils.py  
requirements.txt

## How to Run

Clone repository

git clone https://github.com/yourusername/dev-productivity-tracker

Navigate to project

cd dev-productivity-tracker

Run program

python main.py

Enter path of any Git repository when prompted.

Example

/home/user/projects/myrepo

## Example Output

Developer Productivity Report

Total Commits: 54  
Files Modified: 18  
Lines Added: 1240  
Lines Removed: 230  
Net Code Change: 1010  
Productivity Level: High