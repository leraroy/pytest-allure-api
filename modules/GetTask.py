import pytest

from modules.base_page import BasePage
from helper.config import *


class GetTask(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/task"

    def get_task(self, id):
        return self.sent_request("GET", f"{self.URI}/{id}")

    def get_task_without_auth(self, id):
        return self.sent_request_without_auth("GET", f"{self.URI}/{id}")

    def get_task_schema_validate(self, id):
        return self.validate_schema(func=self.get_task(id).json(), path="get_goal_schema.json")


