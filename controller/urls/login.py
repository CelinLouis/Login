from django.urls import path
from controller.api.login import CreateUserAPI, CustomAuthToken, LogOutAPI, ProfileView,UserProfil

urlpatterns = [
    path('signin/', CreateUserAPI.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('logout/', LogOutAPI.as_view()),
    path('profil/', UserProfil.as_view()),
]