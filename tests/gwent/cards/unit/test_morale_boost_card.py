from unittest import TestCase
from gwent.cards import *


class TestMoraleBoostCard(TestCase):

    def test_init(self):
        morale = MoraleBoostCard("1", "horn1", "Monster", 0, 5, False, False)
        self.assertTrue(morale.morale_boost)

    def test_effect(self):
        # TODO test morale boost effect
        pass
