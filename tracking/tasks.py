from celery import shared_task, signals
import time
import docker
from celery_singleton import Singleton
from .views import init_docker_swarm


# @shared_task(base=Singleton)
# def status_container() -> dict:
#         client = docker.from_env()
#         cs = {}
#         for container in client.containers.list(all=True):
#             # добавить проверку для кэширования
#             if container.attrs["State"]["Running"]:
#                 cs[container.short_id] = True
#             else: cs[container.short_id] = False
#         return cs
# На фон инициализация docker swarm и leave
# @shared_task(base=Singleton)
# def init_docker_swarm():
    # ...

# @shared_task(base=Singleton)
# def leave_docker_swarm():
#     ...