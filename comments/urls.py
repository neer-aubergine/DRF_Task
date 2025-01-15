from django.urls import path
from .views import CommentCreateView

urlpatterns = [
    path('blogs/<int:blog_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:comment_id>/blogs/<int:blog_id>/', CommentCreateView.as_view(), name='comment-delete'),
]
