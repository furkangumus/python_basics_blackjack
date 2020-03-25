# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 2019

@author: kage
"""
import random

SUITS_ = ("Hearts", "Diamonds", "Spades", "Clubs")
RANKS_ = ("two", "three", "four", "five", "six", "seven", "eight", "nine",
          "ten", "jack", "queen",  "king", "ace")
VALUES_ = {
        "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace":11
    }


class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return "{} of {}".format(self.suit, self.rank)


class Deck():
    
    def __init__(self):
        self.deck = list()
        
        for suit in SUITS_:
            for rank in RANKS_:
                self.deck.append(Card(suit, rank))
                
    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += card.__str__() + "\n"
        
        return "The deck contains:\n"+ deck_composition
    
    
    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        return self.deck.pop()
    