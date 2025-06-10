from modules.base_page import BasePage
from helper.config import *
from helper.GeneratorData import GeneratorData

data = GeneratorData()


class UpdateTask(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/task"

    def update_task(self, id, body):
        return self.sent_request("PUT", f"{self.URI}/{id}", body)

    def update_random_name_task(self, id):
        return self.update_task(id, {"name": data.name})

    def update_priority_task(self, id):
        return self.update_task(id, {"priority": data.priority})

    def update_task_with_invalid_ID(self):
        return self.update_task("/111hx1131", {"name": data.name})

    def update_without_auth(self, id):
        return self.sent_request_without_auth("PUT", f"{self.URI}/{id}", {"name": data.name})
