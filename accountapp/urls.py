from django.urls import path

from accountapp.views import comment_list, comment_detail

app_name = "accountapp"

urlpatterns = [
    # function view
    path("comments/", comment_list),
    path("comments_detail/<int:pk>/", comment_detail)
]