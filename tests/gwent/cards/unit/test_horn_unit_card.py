from unittest import TestCase
from gwent.cards import *


class TestHornUnitCard(TestCase):

    def test_init(self):
        horn = HornUnitCard("1", "horn1", "Monster", 0, 5, False, False)
        self.assertTrue(horn.horn)
