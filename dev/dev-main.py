from locust import HttpUser, TaskSet, task, between

from jso import jsonBody, headers


class UserBehaviour(TaskSet):
    @task
    def create_tee_up_task(self):
        self.client.post("/teeups", headers=headers, json=jsonBody)

    @task
    def login_task(self):
        self.client.post("/users/login", {"email": "teeupcreationuser@wuuvo.com", "password": "Pa$$w0rd!qwe"})


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


# zapar777alex@gmail.com
