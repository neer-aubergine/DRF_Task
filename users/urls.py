from django.urls import path
from . import views

urlpatterns = [
    path('', views.usersDetails.as_view()),
    path('<int:pk>/', views.usersDetails.as_view()),

]
