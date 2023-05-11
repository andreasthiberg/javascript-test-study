import os
from dotenv import load_dotenv
from github import Github
import sys
import openpyxl

def get_repo_info():
    load_dotenv()

    repo_url = os.environ.get('CURRENT_REPO')

    args = sys.argv
    if(len(args) > 1):
        repo_url = args[1]

    # Get the  GitHub token
    access_token = os.environ.get('GITHUB_TOKEN')

    # Create a PyGithub object using the access token
    g = Github(access_token)

    # Parse the repository owner and name from the URL
    owner, repo_name = repo_url.split('/')[-2:]

    # Get the repository object from the PyGithub library
    repo = g.get_repo(f'{owner}/{repo_name}')

    # Get all stats
    stars = repo.stargazers_count
    commits = repo.get_commits().totalCount
    watches = repo.subscribers_count
    forks = repo.get_forks().totalCount
    branches = repo.get_branches().totalCount
    releases = repo.get_releases().totalCount
    contributors = repo.get_contributors().totalCount
    desc = repo.description

    # Load the existing Excel workbook
    workbook = openpyxl.load_workbook('data.xlsx')

    # Select the sheet that you want to write data to
    sheet = workbook['Blad1']

    # Find the row with the matching value in column A
    for row in sheet.iter_rows():
        if row[1].value == repo_url:
            matching_row = row[0].row
            break

    ### Write data to excel document.

    # Repo info
    sheet['A{}'.format(matching_row)] = repo_name
    sheet['B{}'.format(matching_row)] = repo_url
    sheet['C{}'.format(matching_row)] = desc
    sheet['Q{}'.format(matching_row)] = watches
    sheet['R{}'.format(matching_row)] = stars
    sheet['S{}'.format(matching_row)] = forks
    sheet['T{}'.format(matching_row)] = commits
    sheet['U{}'.format(matching_row)] = branches
    sheet['V{}'.format(matching_row)] = releases
    sheet['W{}'.format(matching_row)] = contributors

    # Save the changes to the workbook
    workbook.save('data.xlsx')

    print("Data generation complete.")

get_repo_info()