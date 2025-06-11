import pytest
import allure
from modules.CreateTask import CreateTask
from modules.DeleteTask import DeleteTask

@pytest.fixture(scope="class")
def create_task_with_delete():
    with allure.step("Create task with random name"):
        response = CreateTask().create_task_with_random_name()
        data = {
            'name': response.json()['name'],
            'id': response.json()['id']
        }

    yield data

    with allure.step("Delete task"):
        DeleteTask().delete_task(data['id'])

@pytest.fixture(scope="class")
def create_task():
    with allure.step("Create tsk"):
        response = CreateTask().create_task_with_random_name()
        data = {
            'name': response.json()['name'],
            'id': response.json()['id']
        }
        print(f"Name: {data['name']} ID: {data['id']}")

        return data


