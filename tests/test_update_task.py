import allure
import pytest
from modules.GetTask import GetTask
from modules.UpdateTask import UpdateTask
from modules.DeleteTask import DeleteTask

@allure.epic("Tests Update Task")
class TestUpdateTask:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, create_task_with_delete):
        self.get_task = GetTask()
        self.update_task = UpdateTask()
        self.delete_task = DeleteTask()

        self.task_name = create_task_with_delete.get('name')
        self.task_id = create_task_with_delete.get('id')

    @allure.story("test update task and return 200")
    def test_update_task_and_return_200(self):
        response = self.update_task.update_random_name_task(self.task_id)
        with allure.step("Checks status code that returns 200"):
            assert response.status_code == 200

    @allure.story("test update task contain correct name")
    def test_update_task_contain_correct_name(self):
        response = self.update_task.update_random_name_task(self.task_id)
        with allure.step("Checks if the created task name exists in the task list"):
            assert response.json()['name'] in self.get_task.get_task(self.task_id).text

    @allure.story("test update task without authorization")
    def test_update_task_without_auth(self):
        response = self.update_task.update_without_auth(self.task_id)
        with allure.step("Checks status code that returns 400"):
            assert response.status_code == 400
