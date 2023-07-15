from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie.api import views


router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='stream-platform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-details'),

    path('', include(router.urls)),

    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', views.StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('stream/review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]
