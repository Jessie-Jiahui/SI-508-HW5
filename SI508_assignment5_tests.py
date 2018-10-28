## Do not change import statements.
import unittest
from SI508_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code. (That's okay!)
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

# NOTE: test class Card

class test_Card(unittest.TestCase):
    # suit_names should contain a list of strings that represent suits: Diamonds, Clubs, Hearts, Spades
    def test_suit_names(self):
        self.assertEqual(Card().suit_names, ["Diamonds", "Clubs", "Hearts", "Spades"])
    
    # rank_levels should contain a list of integers, 1-13
    def test_rank_levels(self):
        self.assertEqual(Card().suit_names, [1,2,3,4,5,6,7,8,9,10,11,12,13])

    # faces should contain a dictionary whose keys are numbers and whose values are strings.
    def test_faces(self):
        self.assertEqual(Card().faces, {"1":"Ace", "11":"Jack", "12":"Queen", "13":"King"})

    # self.suit, to hold the string name representing the suit of the card
    def test_suit(self):
        self.assertEqual(Card().suit, "Diamonds")

    # self.rank, to hold EITHER the number or the string representation as appropriate of the card rank
    def test_rank_option1(self):
        self.assertEqual(Card().rank, 2)

    # self.rank, to hold EITHER the number or the string representation as appropriate of the card rank
    def test_rank_option2(self):
        self.assertEqual(Card(rank=12).rank, "Queen")

    # self.rank_num, to hold the NUMBER representing the rank (this value should always be an integer)
    def test_rank_num(self):
        self.assertEqual(Card().rank_num, 2)   

    # self.rank, to hold EITHER the number or the string representation as appropriate of the card rank
    def test_rank_num(self):
        self.assertEqual(Card(rank=12).rank_num, 12)

    # The Card class has a string method, which should return a string e.g. "Ace of Spades" or "3 of Clubs", etc.
    def test_string_method_option1(self):
        self.assertEqual(Card(), "2 of Diamonds")

    # The Card class has a string method, which should return a string e.g. "Ace of Spades" or "3 of Clubs", etc.
    def test_string_method_option2(self):
        self.assertEqual(Card(suit=3,rank=1), "Ace of Spades")



# NOTE: test class Deck

class test_Deck(unittest.TestCase):
    # The Deck constructor creates one instance variable: self.cards, which should hold a list of Card objects when a Deck instance is created.
    def test_instance_variable(self):
        self.assertTrue(type(Deck().cards) is list)
    def test_instance_variable(self):
        self.assertTrue(type(Deck().cards[0]) is object)

    # The Deck string method should return a multi-line string with one line for each printed representation of a card in the deck. So a complete deck should have a 52-line string of strings like "Ace of Diamonds", "Two of Diamonds", etc.
    def test_string_method(self):
        self.assertTrue(type(Deck()) is str)
    def test_string_method_face(self):
        faces_diction = {"Diamonds":0 ,"Clubs":0 ,"Hearts":0 ,"Spades":0}
        for face in Card().suit_names:
            for i in Deck().__str__().split("\n"):
                if face in i:
                    faces_diction[face] += 1
        self.assertEqual(faces_diction, {"Diamonds":14 ,"Clubs":14 ,"Hearts":14 ,"Spades":14})

    # Deck has a method pop_card which accepts an integer as input and has a default value such that the Deck will pop off the last (top) card of the deck
    def test_pop_card(self):
        self.assertEqual(Deck().pop_card(), Deck().cards.pop(-1))  

    # Deck has a method replace_card which accepts a Card instance as input.
    def test_replace_card_in(self):
        Deck().replace_card(Card(suit=0,rank=2))
        self.assertEqual(len(Deck().cards), 52) 

    def test_replace_card_not_in(self):
        deck = Deck()
        pop_item1 = deck.pop_card()
        pop_item2 = deck.pop_card()
        deck.replace_card(pop_item1)
        self.assertEqual(len(deck.cards), 51)  

    # Deck has a method sort_cards
    def test_sort_cards(self):
        Deck().shuffle()
        self.assertEqual(Deck().sort_cards()[0:3], ["Ace of Diamonds","2 of Diamonds","3 of Diamonds"])

    # Deck has a method deal_hand which takes a required input hand_size, an integer representing the number of cars in the hand.
    def test_deal_hand_can(self):
        self.assertEqual(Deck().deal_hand(52), True)
    def test_deal_hand_cannot(self):
        Deck().pop_card(2)
        self.assertEqual(Deck().deal_hand(52), False)



# NOTE: test function play_war_game

class test_play_war_game(unittest.TestCase):
    # The play_war_game function should always return a tuple of a string and two integers
    def test_return_type(self):
        self.assertTrue(type(play_war_game()) is tuple)
    def test_return_type_1(self):
        self.assertTrue(type(play_war_game()[0]) is str)
    def test_return_type_1(self):
        self.assertTrue(type(play_war_game()[1]) is int)
    def test_return_type_1(self):
        self.assertTrue(type(play_war_game()[2]) is int)


if __name__ == "__main__":
    unittest.main(verbosity=2)
