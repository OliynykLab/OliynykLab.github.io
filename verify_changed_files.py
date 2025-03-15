import os
from git import Repo

repo_path = os.getcwd()
repo = Repo(repo_path)

changed_files = [item.a_path for item in repo.index.diff(None)]
if changed_files:
    print(f"Changed files: {changed_files}")
else:
    print("No changed files.")