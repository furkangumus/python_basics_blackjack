# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 2019

@author: kage
"""

import game


GAME_STATE = True



def make_bet(chips):
    """
    Takes the chips as parameter and asks user for bet amount.
    """
    while True:
        try:
            chips.bet = int(input("Make your bet >> "))
        except :
            print("Enter an integer please...")
        else:
            if chips.bet > chips.total:
                print(f"You do not have enough chips!"+\
                      " Your balance: {chips.total}")
            else:
                break
            

def hit(deck, hand):
    """
    Gets deck, and the current hand of the user and add a new card to
    user's hand and adjusts the 'ace's. 
    """
    hand.pick_card(deck.deal())
    hand.adjust_aces()
    

def hit_or_stand(deck, hand):
    global GAME_STATE
    
    while True:
        
        hos = input("Hit or Stand [h|S]>> ").upper()
        
        if hos[0] == "H": ## Hit
            hit(deck, hand)
        elif hos[0] == "S": ## Stand
            print("Player stands, Dealer's turn.")
            GAME_STATE = False
        else:
            print("Please enter a valid value. [h | S]...")
            continue
        break


## display summaries...
def short_sum(player, dealer):
    
    print("DEALERS HAND:")
    print(f"One card:\n{dealer.cards[1]}\n")
    print("PLAYERS HAND:")
    for card in player.cards:
        print(card)
        
def full_sum(player, dealer):
    
    print("DEALERS HAND:")
    for card in dealer.cards:
        print(card)
    print("PLAYERS HAND:")
    for card in player.cards:
        print(card)


## result functions...    
def player_busted(player, dealer, chips):
    print("Player busted...")
    chips.lose()


def player_won(player, dealer, chips):
    print("Player won...")
    chips.win()


def dealer_busted(player, dealer, chips):
    print("Player won! dealer busted...")
    chips.win()


def dealer_won(player, dealer, chips):
    print("Dealer won...")
    chips.lose()


def push(player, dealer):
    print("It's a tie. PUSH!!!")
    
    

if __name__ == "__main__":
    
    while True:
        print("...Simple BlackJack...")
        
        ## Setup Deck & Shuffle
        deck = game.deck.Deck()
        deck.shuffle()
        
        ## Setup Dealer & Player
        player = game.Hand()
        player.pick_card(deck.deal())
        player.pick_card(deck.deal())
        
        dealer = game.Hand()
        dealer.pick_card(deck.deal())
        dealer.pick_card(deck.deal())
        
        ## Set up player chips
        player_chips = game.Chip(250)
        
        make_bet(player_chips)
        
        ## Show short summary...
        short_sum(player, dealer)
        
        
        while GAME_STATE:
            
            hit_or_stand(deck, player)
            short_sum(player, dealer)
            
            # if the player hand greater than 21. player busted...
            if player.value > 21:
                player_busted(player, dealer, player_chips)
                
                break
        # If player has not busted, play Dealer's hand until Dealer reaches 17
        if player.value <= 21:
            while dealer.value < 17:
                hit(deck, dealer)
            
            ## show full summary
            full_sum(player, dealer)
            
            if dealer.value > 21: ## Dealer Busted...
                dealer_busted(player, dealer, player_chips)
            elif dealer.value > player.value: ## Dealer Won...
                dealer_won(player, dealer, player_chips)
            elif dealer.value < player.value: ## player wins..
                player_won(player, dealer, player_chips)
            else:
                push(player, dealer)
        
        ### Display Player Status
        print("\nPlayer balance is: {}".format(player_chips.total))
        
        ## do you want to keep playing...
        keep_playing = input("Do you want to keep playing? [y|N] >> ")
        
        if keep_playing.upper() == "Y":
            GAME_STATE = True
            continue
        else:
            print("I hope you won some money today!!!")
            break
        