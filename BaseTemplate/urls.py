# BaseTemplate/urls.py
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.shortcuts import redirect

def go_home(_request):
    return redirect("tournaments:index")

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home (replace with your own landing if desired)
    path("", TemplateView.as_view(template_name="base/home.html"), name="home"),

    #about page
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    # Auth (login/logout/password reset)
    path("accounts/", include("django.contrib.auth.urls")),

    # App: Accounts (register, profile, etc.)
    path("accounts/", include("accounts.urls", namespace="accounts_custom")),

    # App: Tournaments
    path("tournaments/", include(("mavtournaments.urls", "tournaments"), namespace="tournaments")),
]
