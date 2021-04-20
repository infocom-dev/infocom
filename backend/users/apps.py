from django.apps import AppConfig

class UserConfig(AppConfig):
    
    name = 'backend.users'

    def ready(self):
        import backend.api.signals 