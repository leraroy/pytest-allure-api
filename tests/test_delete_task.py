import allure
import pytest

from modules.DeleteTask import DeleteTask
from modules.GetTasks import GetTasks
from modules.CreateTask import CreateTask

@allure.epic("Tests delete task")
class TestDeleteTask:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, create_task):
        self.get_tasks = GetTasks()
        self.create_task = CreateTask()
        self.delete_task = DeleteTask()

        self.task_name = create_task.get('name')
        self.task_id = create_task.get('id')


    @allure.story("test delete task and return 204")
    def test_delete_task_return_204(self):
        response = self.delete_task.delete_task(self.task_id)
        with allure.step("Checks status code that returns 204"):
            assert response.status_code == 204

    @allure.story("test deleted task in tasks list not exists")
    def test_deleted_task_in_get_tasks_not_contain_name_and_id(self):
        self.delete_task.delete_task(self.task_id)
        with allure.step("Checks if the deleted task name not exists in the task list"):
            assert self.task_name not in self.get_tasks.get_tasks().text

    @allure.story("test delete task without authorization")
    def test_delete_task_without_auth(self):
        response = self.delete_task.delete_task_without_auth(self.task_id)
        with allure.step("Checks status code that returns 400"):
            assert response.status_code == 400

    @allure.story("test delete task with invalid ID")
    def test_delete_task_with_invalid_ID(self):
        response = self.delete_task.delete_task_with_invalid_ID()
        with allure.step("Checks status code that returns 401"):
            assert response.status_code == 401

