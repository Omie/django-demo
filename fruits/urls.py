from django.urls import path

from .views import show_all

urlpatterns = [
    path('show-all/', show_all, name="fruits_show_all"),
]
