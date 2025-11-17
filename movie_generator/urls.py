from .views import MovieRecommendationView
from django.urls import path

urlpatterns = [
    path('recommend/', MovieRecommendationView.as_view(), name='movie-recommendations'),
]
