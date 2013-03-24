from django.utils import unittest
from followup.models import Story, FollowUp
from django.test.client import Client
from BeautifulSoup import BeautifulSoup

class AddingItemsTestCase(unittest.TestCase):
    def test_add(self):
        from django.contrib.auth.models import User
        user = User.objects.create_user('add', 'add', 'add')
        url = 'www.example.org'
        c = Client()
        self.assertTrue(c.login(username='add', password='add'))

        response = c.post('/add_url', {'url':url}, follow=True)

        self.assertNotEqual(response.redirect_chain[0][0], 'http://testserver/login?next=/add_url')

        response = c.get('/list')

        soup = BeautifulSoup(response.content)

        items = soup.find(id='items')
        print(items)
        print(items.find_next('ul'))

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.c = Client()

    def test_known_user(self):
        from django.contrib.auth.models import User
        user = User.objects.create_user('unit', 'unit', 'unit')
        self.c.post('/process_login', {'username':'unit', 'password':'unit'})

    def test_unknown_user(self):
        self.c.post('/process_login', {'username':'b', 'password':'b'})

    def test_logout(self):
        self.c.get('/process_logout')
