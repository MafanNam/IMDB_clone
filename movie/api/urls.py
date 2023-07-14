from django.urls import path, include
from movie.api import views


urlpatterns = [
    path('list/', views.MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetailAV.as_view(), name='movie-details')
]