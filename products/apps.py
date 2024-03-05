from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self, *args, **kwargs) -> None:
        import products.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
