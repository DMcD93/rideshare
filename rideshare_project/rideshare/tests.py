"""
Writing test cases
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase, RequestFactory

from .models import Users_Reg, Review
from .views import add_vehicle, search_ride


class TestRideShare(TestCase):

    def setUp(self):
        """
        Setting up all model objects in test database
        :return: None
        """
        #setting up request factory
        self.request = RequestFactory()

        #saving user using django auth
        self.user = User(
            email='sumer.kaur@gmail.com',
            password='sumer@123',
            username='sumer.kaur'
        )
        self.user.save()
        # saving user details in test database
        self.user_reg = Users_Reg(
            user=self.user,
            phone=9987242336,
            age=22,
            identity_number='2226353k'
        )
        self.user_reg.save()

        self.review = Review(
            user=self.user,
            description='An Awesome ride',
            posted_at=datetime.now()
        )
        self.review.save()


#testing user model
    def test_user(self):
        self.assertEqual(
            self.user.username,
            'sumer.kaur',
            'Logged in user changed'
        )

    def test_user_reg(self):
        self.assertEqual(
            self.user_reg.user.username,
            'sumer.kaur',
            'User Registration data should belong to same django auth user looged in'
        )
        self.assertEqual(
            self.user_reg.identity_number,
            '2226353k',
            'User model identity type changed'
        )

    def test_review(self):
        self.assertEqual(
            self.review.user.username,
            'sumer.kaur',
            'User Registration data should belong to same django auth user logged in'
        )

#testing views
    def test_search_ride(self):
        request = self.request.get(
            'search_ride/')
        request.user = self.user
        response = search_ride(request)
        self.assertIsInstance(
            response,
            HttpResponse,
            'Response format should be HttpResponse object'
        )

    def test_add_vehicle(self):
        request = self.request.get(
            'add_vehicle/')
        request.user = self.user
        response = add_vehicle(request)
        self.assertIsInstance(
            response,
            HttpResponse,
            'Response format should be HttpResponse object'
        )


