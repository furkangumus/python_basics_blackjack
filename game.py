# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 2019

@author: kage
"""
import deck

class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
        
    def pick_card(self, card):
        self.cards.append(card)
        self.value += deck.VALUES_[card.rank]
        
        ## tracking aces
        if card.rank == "ace":
            self.aces +=1
            
    
    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            


class Chip():
    
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
        
    
    def win(self):
        self.total += self.bet
    
    
    def lose(self):
        self.total -= self.bet
        