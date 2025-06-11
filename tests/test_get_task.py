import allure
import pytest

from modules.DeleteTask import DeleteTask
from modules.GetTask import GetTask
from modules.CreateTask import CreateTask

@allure.epic("Test Get Task")
class TestGetTask:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, create_task_with_delete):
        self.get_task = GetTask()
        self.create_task = CreateTask()
        self.delete_task = DeleteTask()

        self.task_name = create_task_with_delete.get('name')
        self.task_id = create_task_with_delete.get('id')


    @allure.story("test get task and return 200")
    def test_get_task_return_200(self):
        response = self.get_task.get_task(self.task_id)
        with allure.step("Checks status code that returns 200"):
            assert response.status_code == 200

    @allure.story("test get task contain correct name")
    def test_get_task_contain_correct_name(self):
        response = self.get_task.get_task(self.task_id)
        with allure.step("Checks if the get task contain correct name"):
            assert self.task_name in response.text

    @allure.story("test get task without auth")
    def test_get_task_without_auth(self):
        response = self.get_task.get_task_without_auth(self.task_id)
        with allure.step("Checks status code that returns 400"):
            assert response.status_code == 400

    @allure.story("test get task validate schema")
    def test_get_task_validate_schema(self):
        with allure.step("Check schema is valid"):
            assert self.get_task.get_task_schema_validate(self.task_id) is True