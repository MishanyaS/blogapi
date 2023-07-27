from django.apps import AppConfig


class BlogapiAppConfig(AppConfig):
    """
    Configuration class for the BlogapiApp.

    This class defines the configuration for the BlogapiApp,
    including the default auto-generated primary key field
    and the name of the app.

    Attributes:
        default_auto_field (str): The name of the default
            auto-generated primary key field.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapi_app'
