from django.test import TestCase
from views import *
"""
to test if the user input password matching with the confirm password data
"""
class TestViews(TestCase):
    def test_login(self):
        assert password == confirmpassword
