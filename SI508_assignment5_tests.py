## Do not change import statements.
import unittest
from SI508_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code. (That's okay!)
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
import unittest
import sys
import SI508_cards
from SI508_cards import *

# NOTE: test class Card

class test_Card(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(SystemExit):
            crypt_char("",2) # Testing that function exits if input string not valid
    def test_not_valid_input(self):
        with self.assertRaises(SystemExit):
            crypt_char("um",3) # Testing that function exits if input string not valid

    def setUp(self):
    	self.Card = Card('')

    # length 1 - True
    def test_init_method(self):
        self.assertEqual(check_valid_input("a"), True, "Testing check_valid_input returns True for input with length of one")
    # The Card class has a string method, which should return a string e.g. "Ace of Spades" or "3 of Clubs", etc.
    def test_string_method(self):
        self.assertEqual(check_valid_input("UM"), False, "Testing check_valid_input returns False for input with length of two")

    def tearDown(self):
    self.widget.dispose()

# NOTE: test class Deck

class test_Deck(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(SystemExit):
            crypt_char("",2) # Testing that function exits if input string not valid
    def test_return_type(self):
        self.assertTrue(type(crypt_char("a",6)) is str, "Testing return type is a string")
    # return type string - input digit, assertEqual
    def test_string_method(self):
        self.assertEqual(crypt_char("3",3), "3", "Testing digit imput returns a string digit")
    # return type string - input space, assertEqual
	def test_pop_card(self):
        self.assertEqual(crypt_char("3",3), "3", "Testing digit imput returns a string digit")
	# method replace_card - in
	def test_replace_card_true(self):
        self.assertEqual(crypt_char("3",3), "3", "Testing digit imput returns a string digit")
    # method replace_card - not in
	def test_replace_card_false(self):
        self.assertEqual(crypt_char("3",3), "3", "Testing digit imput returns a string digit")
    # method replace_card
	def test_sort_cards(self):
        self.assertEqual(crypt_char("3",3), "3", "Testing digit imput returns a string digit")
    # method deal_hand - return length
	def test_deal_hand(self):
        self.assertEqual(len(deal_hand(8)), 9, "Testing return the hand_size number of cards")

# NOTE: test class Deck

class play_war_game(unittest.TestCase):
    # test player1 wins
    def test_Player1_win(self):
        with self.assertRaises(SystemExit):
            crypt_char("",2) # Testing that function exits if input string not valid



if __name__ == "__main__":
    unittest.main(verbosity=2)
