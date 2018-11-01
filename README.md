Jiahui Zhou

# SI508 Homework5
#### This code to be tested is based on ideas about decks of "standard 52-deck" playing cards. You can read more about them, if you are unfamiliar, here: https://en.wikipedia.org/wiki/Standard_52-card_deck. I am supposed to write tests to ensure that all of these things in the description that CAN and SHOULD be tested are indeed working as they should. I should write those tests in the file SI508_assignment5_tests.py, including at least 12 test methods. 
## Getting Started
#### This code is written with Python3. You can get view it directly on the Github webpage or make a copy by folking the project and running on your computer. To do that, you should create a GitHub account and downloaded Git properly. 

## Key Files Within
#### INSTRUCTIONS_SI508_HW5.txt is a file that provides the overal instructions about this assignment.
#### code_description_SI508_assignment5.txt includes a description of what a bunch of code ought to do. This is the file I rely on for writing the test code.
#### That code being described is saved in the file SI508_cards.py. The class Card is used to generate Card object, with its suit and rank indicated. The class Deck generates a set of 52 cards. Within that class, users can pop the last card, shuffle the cards, replace the cards, sort cards, and deal-hand cards. The last function play_war_game gives each one a deck, calculates their overall winning counts, and the people who wins more is the final winner.
#### SI508_assignment5_tests.py saved the test code I wrote in, which will test the performance of file SI508_cards.py. I wrote 12 different test methods within 3 classes correpsonding to class Card, class Deck, and function play_war_game. They will function to test unusual cases of the code in the file SI508_cards.py, based on the description.