from django.utils import unittest
from followup.models import Story, FollowUp
from django.test.client import Client
from BeautifulSoup import BeautifulSoup

class AddingItemsTestCase(unittest.TestCase):
    def test_add(self):
        from django.contrib.auth.models import User
        user = User.objects.create_user('add', 'add', 'add')
        url = 'www.example.org/story'
        c = Client()
        self.assertTrue(c.login(username='add', password='add'))

        response = c.post('/add_url', {'url':url}, follow=True)

        self.assertNotEqual(response.redirect_chain[0][0], 'http://testserver/login?next=/add_url')

        response = c.get('/list')

        soup = BeautifulSoup(response.content)

        items = soup.find(id='items')
        items = items.text
        self.assertNotEqual(items.find('example.org/story'), -1)

    def test_response(self):
        c = Client()

        c.login(username='add', password='add')

        response = c.post('/respond_url', {'old':'www.example.org/story', 'new':'www.example.org/update'}, follow=True)

        response = c.get('/list')

        soup = BeautifulSoup(response.content)

        items = soup.find(id='items')
        items = items.text
        self.assertNotEqual(items.find('example.org/update'), -1)

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
