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
    # suit_names should contain a list of strings that represent suits: Diamonds, Clubs, Hearts, Spades; rank_levels should contain a list of integers, 1-13; faces should contain a dictionary whose keys are numbers and whose values are strings.
    def test_class_variables(self):
        self.assertEqual(Card().suit_names, ["Diamonds", "Clubs", "Hearts", "Spades"])
        self.assertEqual(Card().rank_levels, [1,2,3,4,5,6,7,8,9,10,11,12,13])
        self.assertEqual(Card().faces, {1:"Ace", 11:"Jack", 12:"Queen", 13:"King"})

    # The class Card's constructor should accept a number representing a suit and a number representing a rank.
    def test_default_values(self):
        self.assertEqual(Card().suit, "Diamonds")
        self.assertEqual(Card().rank, 2)

    # self.suit, to hold the string name representing the suit of the card; self.rank, to hold EITHER the number or the string representation as appropriate of the card rank; self.rank_num, to hold the NUMBER representing the rank (this value should always be an integer)
    def test_instance_variables(self):
        # test suit
        self.assertTrue(type(Card().suit) is str)
        # test rank
        self.assertEqual(Card(rank=1).rank, "Ace")
        self.assertEqual(Card(rank=11).rank, "Jack")
        self.assertEqual(Card(rank=12).rank, "Queen")
        self.assertEqual(Card(rank=13).rank, "King")
        # test rank_num
        self.assertTrue(type(Card().rank_num) is int)
        for i in range(13):
            self.assertEqual(Card(rank=i+1).rank_num, i+1)

    # The Card class has a string method, which should return a string e.g. "Ace of Spades" or "3 of Clubs", etc.
    def test_card_string_method(self):
        self.assertTrue(type(Card().__str__()) is str)

        list_test = []
        for suit in Card().suit_names:
            for rank in Card().rank_levels:
                if rank in [1,11,12,13]:
                    list_test.append("{} of {}".format(Card().faces[rank], suit))
                else:
                    list_test.append("{} of {}".format(rank, suit))

        list_generate = []
        for suit in range(4):
            for rank in range(13):
                list_generate.append(Card(suit=suit,rank=rank+1).__str__())
        self.assertEqual(list_generate, list_test)



# NOTE: test class Deck

class test_Deck(unittest.TestCase):
    # The Deck constructor creates one instance variable: self.cards, which should hold a list of Card objects when a Deck instance is created.
    def test_instance_variable(self):
        self.assertTrue(type(Deck().cards) is list)
        self.assertEqual(type(Deck().cards[0]), type(Card()))

    # The Deck string method should return a multi-line string with one line for each printed representation of a card in the deck. So a complete deck should have a 52-line string of strings like "Ace of Diamonds", "Two of Diamonds", etc.
    def test_deck_string_method(self):
        faces_diction = {"Diamonds":0 ,"Clubs":0 ,"Hearts":0 ,"Spades":0}
        for face in Card().suit_names:
            for i in Deck().__str__().split("\n"):
                if face in i:
                    faces_diction[face] += 1
        self.assertEqual(faces_diction, {"Diamonds":13 ,"Clubs":13 ,"Hearts":13 ,"Spades":13})

    # Deck has a method pop_card which accepts an integer as input and has a default value such that the Deck will pop off the last (top) card of the deck
    def test_pop_card(self):
        # pop the last item
        self.assertEqual(Deck().pop_card().__str__(), Deck().cards.pop(-1).__str__())  
        # empty list after pop 52 times
        deck = Deck()
        for i in range(52):
            deck.pop_card()
        self.assertEqual(len(deck.cards), 0) 

    # Deck has a method replace_card which accepts a Card instance as input.
    def test_replace_card(self):
        Deck().replace_card(Card(suit=0,rank=2))
        self.assertEqual(len(Deck().cards), 52) 

        deck = Deck()
        pop_item1 = deck.pop_card()
        pop_item2 = deck.pop_card()
        deck.replace_card(pop_item1)
        self.assertEqual(len(deck.cards), 51)  

    # Deck has a method sort_cards
    def test_sort_cards(self):
        deck = Deck()
        deck.shuffle()
        deck.sort_cards()
        self.assertEqual(deck.cards[0].__str__(), "Ace of Diamonds")
        self.assertEqual(deck.cards[1].__str__(), "2 of Diamonds")
        self.assertEqual(deck.cards[2].__str__(), "3 of Diamonds")

    # Deck has a method sort_cards which should organize only the cards that are remaining in the deck (have NOT been removed)
    def test_sort_cards_test_number(self):
        deck = Deck()
        deck.shuffle()
        deck.pop_card()
        deck.sort_cards()
        self.assertEqual(len(deck.cards), 51)

    # Deck has a method deal_hand which takes a required input hand_size, an integer representing the number of cars in the hand.
    def test_deal_hand(self):
        # test return type
        self.assertTrue(type(Deck().deal_hand(1)) is list)
        # test two cases
        self.assertEqual(Deck().deal_hand(52), Deck())
        # deck = Deck()
        # deck.pop_card()
        # self.assertEqual(deck.deal_hand(52), Deck().)



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
