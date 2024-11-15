
import os
import subprocess

def is_git_repo(path):
    try:
        # Check if the .git directory exists
        if os.path.isdir(os.path.join(path, '.git')):
            return True
        # Check if the directory is a git repository
        subprocess.check_output(['git', '-C', path, 'status'], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

current_path = os.getcwd()
if is_git_repo(current_path):
    print("This directory is a Git repository.")
else:
    print("This directory is not a Git repository.")