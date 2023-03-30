from locust import HttpUser, TaskSet, task, between

from create_json import jsonBody, headers


class UserBehaviour(TaskSet):
    @task
    def create_tee_up_task(self):
        self.client.post("/users/register", headers=headers, json=jsonBody)


class User(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(0, 5)
