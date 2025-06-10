from modules.base_page import BasePage


class DeleteTask(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/task"

    def delete_task(self, goal_id):
        return self.sent_request("DELETE", f"{self.URI}/{goal_id}")

    def delete_task_with_invalid_ID(self):
        return self.sent_request("DELETE", f"{self.URI}/b63b8dbe--4147-dc22-d32a405a66bd")

    def delete_task_without_auth(self, goal_id):
        return self.sent_request_without_auth('DELETE', f"{self.URI}/{goal_id}")

