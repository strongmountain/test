import os

from octokit import Octokit


octokit = Octokit(auth='token', token=os.environ.get('GITHUB_TOKEN'))
owner, repo = os.environ.get('GITHUB_REPOSITORY').split('/')
ref = os.environ.get('GITHUB_REF')

number = ref.split('/')[2] if 'pull' in ref else None
octokit.pulls.create_comment(owner=owner, repo=repo, issue_number=number, body="**Action comment**")
