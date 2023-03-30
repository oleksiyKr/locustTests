from locust import HttpUser, TaskSet, task, between

from dev.jso import jsonBody, headers

USER_CREDENTIALS = [
    ("teeupcreationuser@wuuvo.com", "Pa$$w0rd!qwe"),

]


class UserBehaviour(TaskSet):
    # def on_start(self):
    #     if len(USER_CREDENTIALS) > 0:
    #         user, password = USER_CREDENTIALS.pop()
    #         with self.client.post("/users/login", {"email": user, "password": password}) as request:
    #             print(request.json()['accessToken'])

    @task
    def create_tee_up_task(self):
        self.client.post("/teeups", headers=headers, json=jsonBody)

    @task
    def login_task(self):
        user, password = USER_CREDENTIALS.pop()
        self.client.post("/users/login", {"email": user, "password": password})

    # @task
    # def sing_up_task(self):
    #     num = random.randint(10, 500)
    #     jsonReg.update({'email': f'zapar777alex+{num}@gmail.com'})
    #     print(jsonReg.get('email'))
    #     self.client.post("/users/register", headers=headersReg, json=jsonReg)


class User(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(5, 60)

# class UserA(HttpUser):
#     tasks = [UserBehaviour]
#     wait_time = between(5, 10)
#
#
# class StagesShapeWithCustomUsers(LoadTestShape):
#     stages = [
#         {"duration": 10, "users": 10, "spawn_rate": 10, "user_classes": [User]},
#         {"duration": 30, "users": 50, "spawn_rate": 10, "user_classes": [UserA]},
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
