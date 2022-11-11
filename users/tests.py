from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegisterTestCase(TestCase):
    def test_users_account_created(self):
        response = self.client.post(
            reverse('register'),
            data={
                'username': 'test_user',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@user.com',
                'password': 'somepassword'

            }
        )
        user = User.objects.get(username='test_user')

        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'test@user.com')
        self.assertNotEqual(user.password, 'somepassword')
        self.assertTrue(user.check_password('somepassword'))

    def test_requared_fields(self):
        response = self.client.post(
            reverse('register'),
            data={
                'first_name': 'Test',
                'last_name': 'User',
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
            reverse("register"),
            data={
                "username": "test_user",
                "first_name": "test",
                "last_name": "user",
                "email": "testusercom",
                "password": "testpassword"
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')


class LoginTestCase(TestCase):
    def test_user_is_logged(self):
        # user yaratib olamiz
        db_user = User.objects.create_user(username='test_user')
        db_user.set_password('somepassword')
        db_user.save()

        # login page'ga post request yuboramiz
        self.client.post(
            reverse('login'),
            data={
                'username': 'test_user',
                'password': 'somepassword'
            }
        )
        # login qilayotgan client'ni user o'zgaruvchisiga saqlab olamiz
        user = get_user(self.client)
        # is_authenticated metodi orqali kirganini tekshiramiz
        self.assertTrue(user.is_authenticated)

    def test_wrong_password(self):
        # user yaratib olamiz
        db_user = User.objects.create_user(username='test_user')
        db_user.set_password('somepassword')
        db_user.save()

        # login page'ga post request yuboramiz
        self.client.post(
            reverse('login'),
            data={
                'username': 'wrong_user',  # noto'g'ri username kirityapmiz
                'password': 'somepassword'
            }
        )
        # login qilayotgan client'ni user o'zgaruvchisiga saqlab olamiz
        user = get_user(self.client)
        # is_authenticated metodi orqali kirmaganini tekshiramiz
        self.assertFalse(user.is_authenticated)
        # login page'ga post request yuboramiz
        self.client.post(
            reverse('login'),
            data={
                'username': 'test_user',
                'password': 'wrong_passsword'  # noto'g'ri parol kirityapmiz
            }
        )
        # login qilayotgan client'ni user o'zgaruvchisiga saqlab olamiz
        user = get_user(self.client)
        # is_authenticated metodi orqali kirmaganini tekshiramiz
        self.assertFalse(user.is_authenticated)

        # login page'ga post request yuboramiz
        self.client.post(
            reverse('login'),
            data={
                'username': 'test_user',
                'password': 'wrong_passsword'  # noto'g'ri parol kirityapmiz
            }
        )
        # login qilayotgan client'ni user o'zgaruvchisiga saqlab olamiz
        user = get_user(self.client)
        # is_authenticated metodi orqali kirmaganini tekshiramiz
        self.assertFalse(user.is_authenticated)
