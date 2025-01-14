from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view()),
    path('<int:pk>/', views.BlogDetails.as_view()),
]
