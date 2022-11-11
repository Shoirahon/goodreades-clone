from django.contrib.auth import login, get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from books.models import Book


# class BookTestCase(TestCase):
#     def test_no_books(self):
#         response = self.client.get(reverse('book_list'))
#
#         self.assertContains(response, 'No books found.')
#
#     def test_book_list(self):
#         Book.objects.create(title='Book1,description=Description1,isbn=2314253652')
#         Book.objects.create(title='Book2,description=Description2,isbn=1314253656')
#         Book.objects.create(title='Book3,description=Description3,isbn=8314253658')
#
#         response = self.client.get(reverse('book_list'))
#         books = Book.objects.all()
#
#         for book in books:
#             self.assertContains(response, 'book_title')
#
#     def test_book_detail(self):
#         book = Book.objects.create(title='Book1', descriptions='Description1', isbn='2314253652')
#
#         response = self.client.get(reverse('book_detail', kwargs={'id': book.id}))
#
#         self.assertContains(response, book.title)
#         self.assertContains(response, book.description)
#
#
# class ProfileTestCase(TestCase):
#     def test_login_required(self):
#         response = self.client.get(reverse('profile'))
#
#         self.assertEqual(response.url, reverse('login') + '?next=/users/profile/')
#
#     def test_profile_details(self):
#         user = User.objects.create_user(username='test_user', first_name='Test', last_name='User',
#                                         email='test@user.com')
#         user.set_password('somepassword')
#         user.save()
#
#         self.client.login(username='test_user', password='somepassword')
#
#         response = self.client.get(reverse('profile'))
#         self.assertContains(response, user.username)
#         self.assertContains(response, user.first_name)
#         self.assertContains(response, user.last_name)
#         self.assertContains(response, user.email)
