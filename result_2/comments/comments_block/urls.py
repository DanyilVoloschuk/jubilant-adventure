from django.urls import path, include
from rest_framework import routers

from .serializers import CommentSerializer
from .views import *
from .views import index


app_name = "comments_block"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('index/', index),
    path('index/<int:pk>/', CommentDetail.as_view()),
    path('index/delete/<int:pk>/', CommentDetail.as_view()),
    path('index/add/', CommentView.as_view()),
    path('index/edit/<int:pk>/', CommentDetail.as_view()),
    path('block/', CommentView.as_view()),
    path('block/<int:pk>/', CommentView.as_view()),
    path('block/delete/<int:pk>/', CommentView.as_view()),

]
