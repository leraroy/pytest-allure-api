from modules.base_page import BasePage
from helper.config import *
from helper.GeneratorData import GeneratorData

class CreateTask(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/list/{LIST_ID}/task"

    def create_task(self, body):
        response = self.sent_request("POST", self.URI, body)
        self.env_data['id'] = response.json()['id']
        self.env_data['name'] = response.json()['name']
        print(self.env_data)
        return response

    def create_task_with_random_name(self):
        response = self.create_task({"name": GeneratorData().name})
        self.env_data['id'] = response.json()['id']
        self.env_data['name'] = response.json()['name']
        return response

    def create_task_with_file(self):
        print("create data")
        data = self.read_path_body_with_random_fields("example.json")
        print("create task")
        response = self.create_task(data)
        print("Response json")
        print(response.json())
        self.env_data['id'] = response.json()['id']
        self.env_data['name'] = response.json()['name']
        return response

    def create_taskl_without_auth(self):
        return self.sent_request_without_auth("POST", self.URI)

    def create_task_schema_validate(self):
        return self.validate_schema(func=self.create_task_with_random_name().json(), path="create_goal_schema.json")
