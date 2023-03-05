import base64
from pprint import pprint
import time
import os

repository_url = "Safety-Green/SafetyGreen-App"

execute_commands = ["echo 'E O TONHO'"]

from github import Github

# using an access token
g = Github("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")


repo = g.get_repo(repository_url)

lastPush = repo.pushed_at

while True:
    print(f"Last push was at {lastPush}!")

    repo = g.get_repo(repository_url)
    print(f"Real last push is {repo.pushed_at}")
    if lastPush != repo.pushed_at:
        for command in execute_commands:   
            os.system(command)
            break

    time.sleep(5)

