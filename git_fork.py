import requests
import time
from requests.auth import HTTPBasicAuth


class GitFork():
    def __init__(self, url=""):
        self.NAME = "r26zhao"
        self.PASSWORD = "Mangui710"
        self.GITNAME = "noraacy7"
        self.GITPASSWORD = "mangui710"

    def loginGitStar(self):
        r = requests.post("http://gitstar.top:88/api/user/login",
                          params={'username': self.NAME, 'password': self.PASSWORD})
        return r.headers['Set-Cookie']

    def getForkList(self):
        cookie = self.loginGitStar()
        url = "http://gitstar.top:88/api/users/{}/status/fork-recommend".format(self.NAME)
        response = requests.get(url, headers={'Accept': 'application/json', 'Cookie': cookie})
        jsn = response.json()
        list = []
        for obj in jsn:
            list.append(obj['Repo'])
        return list

    def fork(self, url):
        AUTH = HTTPBasicAuth(self.GITNAME, self.GITPASSWORD)
        res = requests.post("https://api.github.com/repos/" + url + "/forks"
                            , headers={'Content-Length': '0'}
                            , auth=AUTH)

    def update_gitstar(self):
        while True:
            url = "http://gitstar.top:88/api/users/{}/forking-repos/update".format(self.NAME)
            res = requests.get(url, headers={'Accept': 'application/json', 'Cookie': self.loginGitStar()})
            print("update:" + str(res.status_code == 200))
            if res.status_code == 200:
                break

if __name__ == '__main__':
    GS = GitFork()
    urls = GS.getForkList()
    for url in urls:
        GS.fork(url)
        print("Forked! -->{}".format(url))
        time.sleep(5.0)
    if len(urls) > 0:
        GS.update_gitstar()