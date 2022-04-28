from django.urls import path

from accountapp.views import comment_list

app_name = "accountapp"

urlpatterns = [
    path("comments/", comment_list)
]