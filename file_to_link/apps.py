from django.apps import AppConfig


class FileToLinkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'file_to_link'

    def ready(self) -> None:
        import file_to_link.signals