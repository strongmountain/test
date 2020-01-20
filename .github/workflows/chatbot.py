import os
import json

from octokit import Octokit


octokit = Octokit(auth='token', token=os.environ.get('GITHUB_TOKEN'))
event = os.environ.get('GITHUB_EVENT')
print(json.loads(event))
# octokit.issues.create_comment(owner=owner, repo=repo, issue_number=number, body=f"**Comment from {os.environ.get('GITHUB_RUN_ID')}**")
