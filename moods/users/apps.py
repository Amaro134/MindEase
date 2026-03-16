from django.apps import AppConfig
import os


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError, ProgrammingError

        admin_email = os.environ.get("ADMIN_EMAIL")
        admin_password = os.environ.get("ADMIN_PASSWORD")
        admin_name = os.environ.get("ADMIN_FULL_NAME", "Admin")

        if not admin_email or not admin_password:
            return

        User = get_user_model()
        try:
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    email=admin_email,
                    password=admin_password,
                    full_name=admin_name,
                )
        except (OperationalError, ProgrammingError):
            # Database not ready (e.g., during initial migrations)
            pass
