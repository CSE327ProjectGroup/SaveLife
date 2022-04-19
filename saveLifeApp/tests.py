from django.test import TestCase

# Create your tests here.

"""
    Testing if user input password matches with confirm password data.
"""


class TestRegister(TestCase):
    def test_register(self):
        assert password == confirmPassword

    def test_organRequest(self):
        assert num.length == '11'
