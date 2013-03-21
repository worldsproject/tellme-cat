from django.utils import unittest
from followup.models import Story, FollowUp
from django.test.client import Client

class WalkThroughTestCase(unittest.TestCase):
    def test_URLs(self):
        c = Client()

        c.login(username='unit', password='unit')
        c.get('/login')
        c.get('/add')
        c.get('/')
        c.get('/respond')
        c.get('/list')

class AddingItemsTestCase(unittest.TestCase):
    def test_add(self):
        url = 'www.example.org'
        c = Client()

        c.login(username='unit', password='unit')

        c.get('/add')
        c.post('/add_url', {'url':url})
        

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
