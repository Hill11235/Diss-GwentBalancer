from unittest import TestCase
from gwent.cards import *
from gwent import *


class TestMedicCard(TestCase):

    def setUp(self):
        self.unitCard = UnitCard("1", "dummy1", "Monster", 0, 8, False, False)
        self.unitHero = UnitCard("2", "dummy2", "Monster", 0, 10, True, True)
        self.med1 = MedicCard("3", "med1", "Northern", 1, 4, False, False)
        self.med2 = MedicCard("4", "med2", "Northern", 1, 4, False, False)

        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)

    def test_get_targets(self):
        self.assertIsNone(self.med1.get_targets(self.board1))

        self.player1.graveyard.append(self.unitCard)
        self.player1.graveyard.append(self.unitHero)

        self.assertEqual(len(self.med1.get_targets(self.board1)), 1)
        self.assertTrue(self.med1.get_targets(self.board1).__contains__(self.unitCard))
        self.assertFalse(self.med1.get_targets(self.board1).__contains__(self.unitHero))

    def test_battlecry(self):
        self.player1.hand.append(self.med1)
        self.player1.graveyard.append(self.unitCard)

        self.med1.place_card(self.board1, None, 1, self.unitCard)
        self.assertTrue(self.board1.rows[1].__contains__(self.med1))
        self.assertTrue(self.board1.rows[0].__contains__(self.unitCard))
        self.assertFalse(self.player1.graveyard.__contains__(self.unitCard))

    def test_chaining_medics(self):
        self.player1.hand.append(self.med1)
        self.player1.graveyard.append(self.med2)
        self.player1.graveyard.append(self.unitCard)

        self.med1.place_card(self.board1, None, 1, self.med2)
        self.assertTrue(self.board1.rows[1].__contains__(self.med1))
        self.assertTrue(self.board1.rows[1].__contains__(self.med2))
        self.assertTrue(self.board1.rows[0].__contains__(self.unitCard))
        self.assertFalse(self.player1.graveyard.__contains__(self.med2))
        self.assertFalse(self.player1.graveyard.__contains__(self.unitCard))

    def test_medic_with_empty_graveyard(self):
        self.player1.hand.append(self.med1)
        self.med1.place_card(self.board1, None, 1, None)
        self.assertTrue(self.board1.rows[1].__contains__(self.med1))
        self.assertEqual(len(self.board1.rows[0]), 0)
        self.assertEqual(len(self.board1.rows[1]), 1)
        self.assertEqual(len(self.board1.rows[2]), 0)
