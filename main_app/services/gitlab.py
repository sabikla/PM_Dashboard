import requests


class GitlabAPI():
    
    def __init__(self, gitlab_url, user_token):
        self.url = gitlab_url
        self.token = user_token

    def fetch_project_list(self):
        header = {"PRIVATE-TOKEN": self.token}
        response = requests.get('https://gitlaburl.com/api/v4/projects?', headers=header)
        print(response.json())
