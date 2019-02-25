from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup

def login(self):
    # Get form build ID to pass back to Drupal on login.
    resp = self.client.get("/")
    parsed_html = BeautifulSoup(resp.text, "html.parser")
    form_build_id = parsed_html.body.find('input', {'name': 'form_build_id'})['value']

    resp = self.client.post("/", {
        "name": "admin",
        "pass": "drupal8",
        "form_id": "user_login_form",
        "form_build_id": form_build_id,
        "op": "Log in"
    })
    print resp

def logout(self):
    self.client.get("/user/logout/")

# Add some pages to load.
def index(self):
    self.client.get("/")

def admin(self):
    self.client.get("/admin/")

class UserBehavior(TaskSet):
    tasks = {index: 1, admin: 1}

    def on_start(self):
        self.client.verify = False
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 8000
    max_wait = 12000

