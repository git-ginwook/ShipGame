import unittest
from ShipGame import ShipGame


class TestShipGame(unittest.TestCase):
    def setUp(self):
        self.sg = ShipGame()

    def test_initialize(self):
        """ check initial settings """
        # empty ships
        self.assertEqual(len(self.sg._battleships["first"]), 0)
        self.assertEqual(len(self.sg._battleships["second"]), 0)

        self.assertEqual(self.sg._num_ships["first"], 0)
        self.assertEqual(self.sg._num_ships["second"], 0)



    def test_placeShip(self):
        """ """
        # if player_str is neither "first" nor "second", return False
        self.assertFalse(self.sg.place_ship("fir", 1, "A1", "R"))
        # if orient_str is neither "R" nor "C", return False
        self.assertFalse(self.sg.place_ship("first", 1, "A1", "Row"))
        # if ship_length < 2, return False
        self.assertFalse(self.sg.place_ship("first", 1, "A1", "R"))
        # if row is a lower case character, return False
        self.assertFalse(self.sg.place_ship("first", 2, "b1", "R"))
        # [head test]
        # if row is out of bound, return False
        self.assertFalse(self.sg.place_ship("first", 2, "X1", "R"))
        # if col is out of bound, return False
        self.assertFalse(self.sg.place_ship("first", 2, "C0", "R"))
        self.assertFalse(self.sg.place_ship("first", 2, "C11", "R"))
        # if passing all validations, add ships and return True
        self.assertTrue(self.sg.place_ship("first", 2, "A1", "R"))
        self.assertTrue(self.sg.place_ship("first", 2, "A10", "C"))
        self.assertTrue(self.sg.place_ship("second", 2, "I8", "R"))
        self.assertTrue(self.sg.place_ship("first", 2, "I10", "C"))
        # [tail test]
        self.assertFalse(self.sg.place_ship("first", 11, "A1", "C"))
        self.assertFalse(self.sg.place_ship("first", 11, "A1", "R"))
        self.assertFalse(self.sg.place_ship("first", 6, "F6", "C"))
        self.assertFalse(self.sg.place_ship("first", 6, "F6", "R"))
        # [overlap test]
        self.sg.place_ship("first", 4, "F10", "C")
        # check _battleships and _num_ships
        self.assertEqual(len(self.sg._battleships["first"]), 3)
        self.assertIn("B10", self.sg._battleships["first"][1])
        self.assertEqual(self.sg._num_ships["first"], 3)
        self.assertEqual(len(self.sg._battleships["second"]), 1)
        self.assertIn("I9", self.sg._battleships["second"][0])
        self.assertEqual(self.sg._num_ships["second"], 1)

    def tearDown(self):
        # self.widget.dispose()
        pass


if __name__ == '__main__':
    unittest.main()
