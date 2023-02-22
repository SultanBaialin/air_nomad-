from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewCreateAPIView.as_view()),   # api/v1/reviews POST
    path('reviews/<int:pk>/', views.ReviewUpdateDeleteApiView.as_view()),
]