from django.apps import AppConfig


class ContactsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacts_app'

    def ready(self):
        import contacts_app.signals