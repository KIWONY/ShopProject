from django.urls import path

from accountapp.views import comment_list, comment_detail, CommentListView, CommentDetailView, CommentAPIView

app_name = "accountapp"

urlpatterns = [
#api view
    path("generic/<int:id>/",CommentAPIView.as_view()),

# class view
    path("comments/", CommentListView.as_view()),
    # path("comments/", comment_list),

# function view
    path("comments_detail/<int:id>/", CommentDetailView.as_view()),
    # path("comments_detail/<int:pk>/", comment_detail)
]