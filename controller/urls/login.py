from django.urls import path
from controller.api.login import CreateUserAPI, CustomAuthToken, LogOutAPI

urlpatterns = [
    path('signup/', CreateUserAPI.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('logout', LogOutAPI.as_view()),
]