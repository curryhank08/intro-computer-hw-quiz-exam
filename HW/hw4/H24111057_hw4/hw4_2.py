"""
@author: H24111057 統計系 姚博瀚
# Blackjack game (21點) with computer 
"""

import random

def create_52cards():
    ranks = [x for x in range(1, 14)]
    suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
    deck = [(x, y) for x in ranks for y in suits]
    return deck

def create_52cards2():
    ranks = [x for x in range(1, 14)]
    suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
    deck = [(x, y) for x in ranks for y in suits]
    return deck

def initial_cards(deck):
    deck = create_52cards()
    # print("deck: ", deck)

    # hit 4 cards from deck
    hits = random.sample(deck, 4)
    # remove hitted card from deck
    for hit in hits:
        deck.remove(hit)
    # print("hits: ", hits)
        
    # hit 2 cards from hits list repectively for player and dealer
    player_cards = []
    dealer_cards = []
    hits2 = random.sample(hits, 2)
    # print("hits2: ", hits2)
    # append the hitted 2 cards (hits2) into player's cards
    for i in hits2:
        player_cards.append(i)
    # remove the hittd 2 cards (hits2) from hits
    for r in hits2:
        hits.remove(r)
    # append the rest 2 cards (hits) into dealer's cards
    for j in hits:
        dealer_cards.append(j)
        
    return player_cards, dealer_cards

    # print("player's cards: ", player_cards)
    # print("dealer's cards: ", dealer_cards)

# value a single card
def card_value(card):
    rank = card[0]
    # suit = card[1]
    
    if rank in range(11,14):
        return 10
    elif rank == 1:
        return 11
    else:
        return int(rank)

# value total cards in one's hand
def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    number_of_aces = sum(card[0] == 1 for card in hand)

    while value > 21 and number_of_aces >= 1:
        value -= 10
        number_of_aces -= 1
    return value

'''wrong:
def formatted_hand(hand):
    for card in hand:
        if card[0] in range(11, 14):
            if card[0] == 11:
                str(card[0]).replace('JACK')
            elif card[0] == 12:
                str(card[0]).replace('QUEEN')
            else: # rank = 13 -> King
                str(card[0]).replace('KING')
    hand_list = ['{rank}-{suit}'.format(rank=card[0], suit=card[1]) for card in hand]
    formatted_hand = ', '.join(hand_list)
    return formatted_hand
'''
# transform the list of someone's all cards (player_hand or dealer_hand) (ex. [(1 # rank, 'KING' # suit), (3, 'CLUB'), (11, 'DIAMOND')])
# into a string which each card connected by a ','. (ex. 'ACE-KING, 3-CLUB, JACK-DIAMOND') 
def formatted_hand(hand):
    formatted_hand_list = []
    for card in hand:
        rank = card[0]
        suit = card[1]
        if rank in [1, 11, 12, 13]:
            if rank == 1:
                rank = 'ACE'
            elif rank == 11:
                rank = 'JACK'
            elif rank == 12:
                rank = 'QUEEN'
            elif rank == 13:
                rank = 'KING'
        formatted_hand_list.append('{rank}-{suit}'.format(rank=rank, suit=suit))
        formatted_hand = ', '.join(formatted_hand_list)
    return formatted_hand

# transform a single card (player's hit or dealer's hit) (ex. (1 # rank, 'KING' # suit) )
# into a string. (ex. 'ACE-KING') 
def formatted_singe_card(card):
    rank = card[0]
    suit = card[1]
    if rank == 1:
        rank = 'ACE'
    elif rank == 11:
        rank = 'JACK'
    elif rank == 12:
        rank = 'QUEEN'
    elif rank == 13:
        rank = 'KING'
        
    formatted_card = '{rank}-{suit}'.format(rank = rank, suit = suit)
    return formatted_card
    
def game_logic(player_hand, dealer_hand, deck):
    # player
    while True:
        # to control whether turns to dealer's round
        player_busts = False
        
        player_value = hand_value(player_hand)
        print("Your current value is Blackjack! (21)" if player_value == 21
            else "Your current value is {total_value}.".format(total_value = player_value)
            )
        formatted_player_hand = formatted_hand(player_hand)
        print("With the hand: {}".format(formatted_player_hand))
        print()
        
        action = int(input("Hit or stay? (Hit = 1, Stay = 0): "))
        
        # player decides to hit
        if action == 1:
            hit = random.choice(deck)
            formatted_player_hit = formatted_singe_card(hit)
            print("You draw {}.".format(formatted_player_hit))
            deck.remove(hit)
            player_hand.append(hit)
            player_value = hand_value(player_hand)
            print()
            # Blackjack
            if player_value == 21:
                print("Your current value is Blackjack! (21)")
                formatted_player_hand = formatted_hand(player_hand)
                print("With the hand: {}.".format(formatted_player_hand))
                break
            # busts
            elif player_value > 21:
                print("Your current value is bust! (>21)")
                formatted_player_hand = formatted_hand(player_hand)
                print("With the hand: {}.".format(formatted_player_hand))
                player_busts = True
                break
            '''
            # do not bust
            else:
            '''                
        # player decides to stay (action == 0)
        else:
            break
    
    # dealer
    while (player_busts == False):
        print()
        dealer_value = hand_value(dealer_hand)
        print("Dealer's current value is {total_value}.".format(total_value = dealer_value))   
        formatted_dealer_hand = formatted_hand(dealer_hand)
        print("With the hand: {}.".format(formatted_dealer_hand))
        
        while hand_value(dealer_hand) < 17:
            hit2 = random.choice(deck)
            formatted_dealer_hit = formatted_singe_card(hit2)
            print()
            print("Dealer draw {}.".format(formatted_dealer_hit))
            deck.remove(hit2)
            dealer_hand.append(hit2)
            dealer_value = hand_value(dealer_hand)
            
            print()
            if 17 < dealer_value <= 20:
                print("Dealer's current value is {total_value}.".format(total_value = dealer_value))
                formatted_dealer_hand = formatted_hand(dealer_hand)
                print("With the hand: {}.".format(formatted_dealer_hand))
                
            elif dealer_value == 21:
                print("Dealer's current value is Blackjack! (21)")            
                formatted_dealer_hand = formatted_hand(dealer_hand)
                print("With the hand: {}.".format(formatted_dealer_hand))
            
            elif dealer_value > 21:
                print("Dealer's current value is Bust! (>21)")            
                formatted_dealer_hand = formatted_hand(dealer_hand)
                print("With the hand: {}.".format(formatted_dealer_hand))
        break
    
# Compare the player's and dealer's hands and declare the winner based on the game rules
def determine_winner(player_hand, dealer_hand):
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)
    print()
    
    if player_value == dealer_value:
        print("*** You tied the dealer, nobody wins. ***")
    elif player_value == 21:
        print("*** You beat the dealer! ***")
    elif dealer_value == 21:
        print("*** Dealer wins! ***")
    elif player_value > 21:
        print("*** Dealer wins! ***")
    elif dealer_value > 21:
        print("*** You beat the dealer! ***")
    elif ((player_value and dealer_value < 21) 
          and (player_value > dealer_value)):
        print("*** You beat the dealer! ***")
    elif ((player_value and dealer_value < 21) 
          and (player_value < dealer_value)):
        print("*** Dealer wins! ***")
        

# main game loop, allowing the player to decide whether to play again or not.
def main():
    while True:
        deck = create_52cards()
        player_hand, dealer_hand = initial_cards(deck)
        game_logic(player_hand, dealer_hand, deck)
        determine_winner(player_hand, dealer_hand)
        quit_game = True
        
        # ask user play again or not
        while True:
            ask = input("Want to play again? (y/n): ")
            try:
                if ask.lower() == 'y':
                    print("-"*50)
                    break
                elif ask.lower() == 'n':
                    quit_game = False
                    break
            except ValueError:
                print("Invalid input! try again. (y/n)")
        
        if quit_game is False:
            break
        
# run the Blackjack game
main()