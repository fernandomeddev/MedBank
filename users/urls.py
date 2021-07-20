from django.conf.urls import url
from . import views
from .views import Historico

app_name = "users"

urlpatterns = [
        url(r"^account_status/$", views.index, name = "account_status"),
        url(r"^money_transfer/", views.money_transfer, name = "money_transfer"),
        url(r"report/$", Historico.as_view(), name = "report"),
        url(r"help/$", views.help, name = "help"),
        url(r"edit_details/", views.edit_details, name = "edit_details"),
        url(r"delete_account/$", views.delete_account, name = "delete_account")
    ]
