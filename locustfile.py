import time
from locust import HttpUser, task, between
from helper.config import *
from helper.GeneratorData import GeneratorData
class PerformanceTest(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    def view_items(self):
        self.client.get(f"/api/v2/list/{LIST_ID}/task",
                        headers={"Authorization": TOKEN})

    def on_start(self):
        self.client.post(f"/api/v2/list/{LIST_ID}/task",
                         headers={"Authorization": TOKEN},
                         json={"name": GeneratorData().name})
