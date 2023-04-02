from abc import ABC, abstractmethod
from enum import IntEnum
from random import randrange
import sys
import unittest


class Suit(IntEnum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3
    
    def getSuitFromValue(self, value):
        return Suit(value).name


class Card():
    def __init__(self, face_value, suit):
        self.available = True
        self.face_value = face_value
        self.suit = suit
    
    @abstractmethod
    def value(self):
        pass
    
    def suit(self):
        return self.suit
    
    def is_available(self):
        return self.available
    
    def mark_available(self):
        self.available = True
    
    def mark_unavailable(self):
        self.available = False

class Deck(Card):
    def __init__(self):
        self.cards = []
        self.dealt_index = 0
        
    def set_deck_of_cards(self, cards):
        self.cards = cards
    
    def shuffle(self):
         for i in range(len(self.cards)-1):
            random_index = randrange(i+1, len(self.cards))
            self.cards[i], self.cards[random_index] = self.cards[random_index], self.cards[i]
    
    def remaining_cards(self):
        return len(self.cards) - self.dealt_index
    
    def draw_card(self):
        return self.cards.pop()

    def deal_hand(self, number):
        if self.remaining_cards() < number:
            return None
        hand = list()
        for i in range(number):
            card = self.deal_card()
            if card:
                hand[i] = card
        return hand
    
    def deal_card(self):
        if self.remaining_cards() == 0:
            return None
        card = self.cards[self.dealt_index]
        card.mark_unavailable()
        self.dealt_index += 1
        return card
    
class Hand(Card):
    def __init__(self):
        self.cards = []
    
    def score(self):
        score = 0
        for i in range(len(self.cards)):
            score += self.cards[i].value
        return score
    
    def add_card(self, card):
        self.cards.append(card)
        

class BlackJackCard(Card):
    def __init__(self, face_value, suit):
        super().__init__(face_value, suit)
    
    def is_ace(self):
        return self.face_value == 1
    
    def is_face_scared(self):
        return self.face_value >= 11 and self.face_value <= 13

    def value(self):
        if self.is_ace():
            return 1
        elif self.face_value >= 11 and self.face_value <= 13:
            return 10
        else:
            return self.face_value
    
    def min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.value()
    
    def max_value(self):
        if self.is_ace():
            return 11
        else:
            return self.value() 
        
class BlackJackHand(BlackJackCard):
    def score(self):
        scores = self.possible_scores()
        max_under = -sys.maxsize - 1
        min_over = sys.maxsize
        for score in scores:
            if score > 21 and score < min_over:
                min_over = score
            elif score <= 21 and score > max_under:
                max_under = score
        return min_over if max_under == -sys.maxsize - 1 else max_under
    
    def possible_scores(self):
        scores = list()
        if self.cards and len(self.cards) > 0:
            scores.append(0)
            for card in self.cards:
                for i in range(len(scores)):
                    if card.is_ace():
                        scores.append(scores[i]+card.max_value())
                    scores[i] += card.min_value()
        return scores
    
    def busted(self):
        return self.scores() > 21
    
    def is_21(self):
        return self.scores() == 21
    
    def is_black_jack(self):
        if len(self.cards) != 2:
            return False
        return (self.cards[0].is_ace() and self.cards[1].is_face_scared()) or \
                (self.cards[1].is_ace() and self.cards[0].is_face_scared())
                

class Test(unittest.TestCase):
    def test_card_deck(self):
        cards = [Card(2, "Hearts"), Card(4, "Clubs")]
        deck = Deck()
        deck.set_deck_of_cards(cards)
        self.assertEqual(deck.draw_card().suit, "Clubs")

if __name__ == "__main__":
    unittest.main()