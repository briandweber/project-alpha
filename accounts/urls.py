from django.urls import path
from accounts.views import user_login, user_logout, user_signup, profile


urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", user_signup, name="signup"),
    path("profile/", profile, name="edit_user")
]
