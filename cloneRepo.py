import os
import git
from dotenv import load_dotenv


load_dotenv()
repo_dir = "./testRepo"
repo_url = os.environ.get('CURRENT_REPO')
git.Repo.clone_from(repo_url, repo_dir)
# Install the project's dependencies using npm
os.chdir(repo_dir)
os.system("npm install")