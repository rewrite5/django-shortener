from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("s/<str:hash>", views.shorten, name="shorten"),
]
