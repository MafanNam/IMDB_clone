from django.urls import path
from movie.api import views


urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='stream-detail'),

    path('stream/<int:pk>/review/', views.StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('stream/review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),
]
