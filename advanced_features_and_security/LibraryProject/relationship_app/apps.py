from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
    
    def ready(self):
        from bookshelf.models import UserProfile

        # import relationship_app.signals
