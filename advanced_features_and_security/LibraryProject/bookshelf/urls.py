from importlib.resources import path
from . import views

urlpatterns = [
    # ... other paths ...
    path('raise/', views.raise_exception, name='raise_exception'),
]
