import allure
import pytest

from modules.DeleteTask import DeleteTask
from modules.GetTasks import GetTasks
from modules.CreateTask import CreateTask

@allure.epic("Tests Get Tasks")
class TestGetTasks:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, create_task_with_delete):
        self.get_tasks = GetTasks()
        self.create_task = CreateTask()
        self.delete_task = DeleteTask()

        self.task_name = create_task_with_delete.get('name')
        self.task_id = create_task_with_delete.get('id')

    @allure.story("Test get tasks and return 200")
    def test_get_tasks_return_200(self):
        response = self.get_tasks.get_tasks()
        with allure.step("Check status code is 200"):
            assert response.status_code == 200

    @allure.story("Test get tasks contain correct name")
    def test_get_tasks_contain_correct_name(self):
        response = self.get_tasks.get_tasks()
        with allure.step(f"Checks if the {self.task_name} name exists in the task list"):
            assert self.task_name in response.text

    @allure.story("Test get tasks without authorization")
    def test_get_tasks_without_auth(self):
        response = self.get_tasks.get_tasks_without_auth()
        with allure.step("Check status code is 400"):
            assert response.status_code == 400

    # @allure.story("Test get tasks has valid schema")
    # def test_get_tasks_validate_schema(self):
    #     result = self.get_tasks.get_tasks_schema_validate()
    #     with allure.step("Check schema is valid"):
    #         assert result is True
