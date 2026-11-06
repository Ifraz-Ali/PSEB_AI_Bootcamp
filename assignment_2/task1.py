import requests

usernames = ["Ifraz-Ali", "ZameerGabolGithub", "Babar860"]

for username in usernames:
    r = requests.get(f"https://api.github.com/users/{username}")
    if r.status_code == 200:
        data = r.json()
        print("Username:", data["login"])
        print("Public Repositories:", data["public_repos"])
    else:
        print(f"Failed to fetch data for {username}. Status code: {r.status_code}")
