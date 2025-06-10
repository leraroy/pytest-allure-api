import allure

from modules.base_page import BasePage
from helper.config import *


class GetTasks(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/list/{LIST_ID}/task"

    def get_tasks(self):
        return self.sent_request("GET", self.URI)

    def get_tasks_without_auth(self):
        return self.sent_request_without_auth("GET", self.URI)

    def get_tasks_schema_validate(self):
        return self.validate_schema(func=self.get_tasks().json(), path="get_tasks_schema.json")


