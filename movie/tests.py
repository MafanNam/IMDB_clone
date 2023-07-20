from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


from movie import models


class StreamPlatformTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test', password='newpassword123')
        self.token = Token.objects.get(user__username='test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name='Netflix',
                                                           about='Test',
                                                           website='https://netflix.com', )

    def test_streamplatform_create(self):
        data = {
            'name': 'Netflix',
            'about': 'Test',
            'website': 'https://netflix.com',
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test', password='newpassword123')
        self.token = Token.objects.get(user__username='test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name='Netflix',
                                                           about='Test',
                                                           website='https://netflix.com', )
        self.watchlist = models.WatchList.objects.create(platform=self.stream,
                                                         title='Test', storyline='test story',
                                                         active=True)

    def test_watchlist_create(self):
        data = {
            'platform': self.stream,
            'title': 'Test',
            'storyline': 'test story',
            'active': True,
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie-details', args=(self.watchlist.id,)))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(models.WatchList.objects.count(), 1)
        self.assertEquals(models.WatchList.objects.get().title, 'Test')


class ReviewTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test', password='newpassword123')
        self.token = Token.objects.get(user__username='test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name='Netflix', about='Test',
                                                           website='https://netflix.com', )
        self.watchlist = models.WatchList.objects.create(platform=self.stream,
                                                         title='Test', storyline='test story',
                                                         active=True)
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream,
                                                          title='Test2', storyline='test2 story',
                                                          active=True)
        self.review = models.Review.objects.create(review_user=self.user, rating=5, description='good movie',
                                                   watchlist=self.watchlist2, active=True)

    def test_review_create(self):
        data = {
            'review_user': self.user,
            'rating': 5,
            'description': 'Good',
            'watchlist': self.watchlist,
            'active': True
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_review_create_unauth(self):
        data = {
            'review_user': self.user,
            'rating': 5,
            'description': 'Good',
            'watchlist': self.watchlist,
            'active': True
        }
        self.client.force_authenticate(user=None, token=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            'review_user': self.user,
            'rating': 4,
            'description': 'Good(update)',
            'watchlist': self.watchlist,
            'active': False
        }
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(models.Review.objects.count(), 1)
        self.assertEquals(models.Review.objects.get().description, 'Good(update)')

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_review_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        response = self.client.get('/api/reviews/?username' + self.user.username)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

