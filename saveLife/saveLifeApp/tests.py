from django.test import TestCase
import pytest
from views import *


class TestViews(TestCase):

  def test_donation(self):
    x = len(donorNum)
    y: int = 11
    assert (x, y)

  def test_after_death(self):
     x = len(donorNid)
     y: int = 10
     assert (x, y)
