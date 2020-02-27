import os
import json

from octokit import Octokit


octokit = Octokit(auth="token", token=os.environ.get("GITHUB_TOKEN"))
owner, repo = os.environ.get("GITHUB_REPOSITORY").split("/")
ref = os.environ.get("GITHUB_REF")

number = ref.split("/")[2] if "pull" in ref else None
octokit.issues.create_comment(
    owner=owner, repo=repo, issue_number=number, body=f"**Comment from {os.environ.get('GITHUB_RUN_ID')}**"
)

event_path = os.environ.get("GITHUB_EVENT_PATH")
with open(event_path) as event_file:
    event = json.load(event_file)

params = {"name": "check run!", "head_sha": event["pull_request"]["head"]["sha"]}
octokit.checks.runs.create_a_check_run(owner=owner, repo=repo, **params)
