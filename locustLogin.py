from locust import HttpLocust, TaskSet
from bs4 import BeautifulSoup

def login(self):
    response = self.client.get("/user")
    parsed_html = BeautifulSoup(response.text, "html.parser")
    form_build_id = parsed_html.select('input[name="form_build_id"]')[0]["value"]
    print response
    print form_build_id

    r = self.client.post("/user", {
    "name":"admin",
    "pass":"drupal8",
    "form_id": "user_login_form",
    "op": "Log+in",
    "form_build_id": form_build_id
    })
    print r

def logout(self):
    self.client.get("/user/logout/")

def index(self):
    self.client.get("/")

def nodeadd(self):
    self.client.get("/admin/")

class UserBehavior(TaskSet):
    tasks = {index: 1, nodeadd: 1}

    def on_start(self):
        self.client.verify = False
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 8000
    max_wait = 12000
