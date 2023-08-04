import datetime

from locust import HttpUser, TaskSet, between, task

from user_data import headers, jsonBody

USER_CREDENTIALS = [
    ("coowetest999+locust@gmail.com", "Pa$$w0rd!"),
]

start_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
ended_time = start_time + datetime.timedelta(hours=1)


class UserBehaviour(TaskSet):
    resp = {}

    def on_start(self):
        if len(USER_CREDENTIALS) > 0:
            user, password = USER_CREDENTIALS.pop()
            with self.client.post("/users/login", {"email": user, "password": password,
                                                   "type": "email"}) as request:
                global resp
                resp = request.json()

    @task
    def create_tee_up_task(self):
        token = resp['accessToken']
        id = resp['id']
        headers['authorization'] = f'Bearer {token}'
        jsonBody['ownerId'] = id
        jsonBody["gameplanOptions"][0]["suggestions"][0]["endDate"] = ended_time.isoformat()
        jsonBody["gameplanOptions"][0]["suggestions"][0]["startDate"] = start_time.isoformat()

        self.client.post("/teeups", headers=headers, json=jsonBody)


class User(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(0, 5)

# class StagesShapeWithCustomUsers(LoadTestShape):
#     stages = [
#         {"duration": 30, "users": 3000, "spawn_rate": 10, "user_classes": [User]},
#         # {"duration": 60, "users": 100, "spawn_rate": 10, "user_classes": [UserB]},
#         # {"duration": 120, "users": 100, "spawn_rate": 10, "user_classes": [UserA,UserB]},
#     ]
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         for stage in self.stages:
#             if run_time < stage["duration"]:
#                 try:
#                     tick_data = (stage["users"], stage["spawn_rate"], stage["user_classes"])
#                 except:
#                     tick_data = (stage["users"], stage["spawn_rate"])
#                 return tick_data
#
#         return None
