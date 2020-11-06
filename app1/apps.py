from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'app1'

    def ready(self):
        import app1.signals




