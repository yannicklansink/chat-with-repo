import os
from dotenv import load_dotenv
from langchain.document_loaders import GitLoader

# This function call loads environment variables from a .env file located in the same directory (or parent directories) as the script, 
# or from a default location. Once executed, environment variables set in the .env file become accessible through os.environ.
load_dotenv()

loader = GitLoader(
    clone_url=os.environ.get("REPO_URL"),
    repo_path='repo',
    branch=os.environ.get("REPO_BRANCH"),
)

loader.load()