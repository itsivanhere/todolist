from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("tasks/<str:task_id>/delete", views.delete, name="delete-task"),
    path("tasks/<str:task_id>/edit", views.edit, name="edit-task")
]
