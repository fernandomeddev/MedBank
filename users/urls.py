from django.urls.conf import path 
from . import views
from .views import Historico

app_name = "users"

urlpatterns = [
        path("account_status/", views.index, name = "account_status"),
        path("money_transfer/", views.money_transfer, name = "money_transfer"),
        path("report/", Historico.as_view(), name = "report"),
        path("help/", views.help, name = "help"),
        path("edit_details/", views.edit_details, name = "edit_details"),
        path("delete_account/", views.delete_account, name = "delete_account")
    ]
