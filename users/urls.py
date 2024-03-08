from django.urls import path
from django.contrib import admin
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", views.login, name="login"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name='index.html'), name="logout")
    ]