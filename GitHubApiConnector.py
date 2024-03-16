import requests

class GitHubApiConnector:
    BASE_URL = "https://api.github.com/repos"

    def __init__(self, token):
        self.token = token

    def fetch_repository_contents(self, username, repository_name, file_extension):
        headers = {"Authorization": f"Bearer {self.token}"}
        url = f"{self.BASE_URL}/{username}/{repository_name}/contents/"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return [file for file in response.json() if file['name'].endswith(file_extension)]
        else:
            raise Exception(f"Failed to fetch repository contents: {response.status_code}")

    def fetch_file_content(self, file_url):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(file_url, headers=headers)
        if response.status_code == 200:
            return response.content, response.encoding
        else:
            raise Exception(f"Failed to fetch file content: {response.status_code}")
