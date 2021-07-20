from django.urls import path
from .views import AboutPageView, HomePageView
from pages import views
from django.urls.conf import path

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]