import allure
import pytest
from modules.GetTasks import GetTasks
from modules.CreateTask import CreateTask
from modules.DeleteTask import DeleteTask

@allure.epic("Tests Create Task")
class TestCreateTask:

    @pytest.fixture(autouse=True)
    def setup(self):

        self.get_tasks = GetTasks()
        self.delete_task = DeleteTask()
        self.create_task = CreateTask()

    @allure.story("test create task and return 200")
    def test_create_task_and_return_200(self):
        with allure.step("Checks status code that returns 200"):
            assert self.create_task.create_task_with_random_name().status_code == 200

    @allure.story("test create task with valid body from file")
    def test_create_task_with_valid_body_from_file_with_correct_name(self):
        response = self.create_task.create_task_with_file()
        with allure.step("Checks if the created task name exists in the task list"):
            assert response.json()['name'] in self.get_tasks.get_tasks().text

    @allure.story("test create task without authorization")
    def test_create_task_without_auth(self):
        with allure.step("Checks status code that returns 400"):
            assert self.create_task.create_taskl_without_auth().status_code == 400

    @allure.story("test create task has valid schema")
    def test_create_task_validate_schema(self):
        with allure.step("Check schema is valid"):
            assert self.create_task.create_task_schema_validate()

    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        yield
        with allure.step("Delete task"):
            self.delete_task.delete_task(self.create_task.env_data.get('id'))