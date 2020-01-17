import os

from octokit import Octokit


octokit = Octokit(auth='token', token=os.environ.get('GITHUB_TOKEN'))
print(octokit.repos.list().json)
