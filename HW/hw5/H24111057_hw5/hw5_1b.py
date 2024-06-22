"""
@author: H24111057 統計系 姚博瀚
# Blackjack game (21點) with computer 
"""

import random

def create_52cards():
    # Create a standard 52-card deck
    ranks = [x for x in range(1, 14)]  # 1 to 13 (Ace to King)
    suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
    deck = [(x, y) for x in ranks for y in suits]
    return deck

def initial_cards(deck):
    # Initialize the game by dealing cards to the player and dealer
    deck = create_52cards()

    # Draw 4 cards from the deck
    hits = random.sample(deck, 4)
    # Remove drawn cards from the deck
    for hit in hits:
        deck.remove(hit)
        
    # Split the 4 cards into 2 for the player and 2 for the dealer
    hits2 = random.sample(hits, 2)
    player_cards = hits2
    dealer_cards = [card for card in hits if card not in hits2]

    # Convert lists to dictionaries for better readability
    player_hand = {'cards': player_cards, 'value': hand_value(player_cards)}
    dealer_hand = {'cards': dealer_cards, 'value': hand_value(dealer_cards)}
        
    return player_hand, dealer_hand, deck

def card_value(card):
    # Calculate the value of a single card
    rank = card[0]
    
    if rank in range(11,14):  # Jack, Queen, King
        return 10
    elif rank == 1:  # Ace
        return 11
    else:  # Number cards (2-10)
        return int(rank)

def hand_value(hand):
    # Calculate the total value of all cards in a hand
    value = sum(card_value(card) for card in hand)
    number_of_aces = sum(card[0] == 1 for card in hand)

    # Adjust for Aces (can be 1 or 11)
    while value > 21 and number_of_aces >= 1:
        value -= 10  # Change an Ace from 11 to 1
        number_of_aces -= 1
    return value

def formatted_hand(hand):
    # Convert a hand (list of tuples) into a readable string
    formatted_hand_list = []
    for card in hand:
        rank, suit = card
        if rank == 1: rank = 'ACE'
        elif rank == 11: rank = 'JACK'
        elif rank == 12: rank = 'QUEEN'
        elif rank == 13: rank = 'KING'
        formatted_hand_list.append(f'{rank}-{suit}')
    return ', '.join(formatted_hand_list)

def formatted_single_card(card):
    # Convert a single card (tuple) into a readable string
    rank, suit = card
    if rank == 1: rank = 'ACE'
    elif rank == 11: rank = 'JACK'
    elif rank == 12: rank = 'QUEEN'
    elif rank == 13: rank = 'KING'
    return f'{rank}-{suit}'

def game_logic(player_hand, dealer_hand, deck):
    # Main game logic for player's and dealer's turns

    # Player's turn
    while True:
        player_busts = False
        
        # Display player's current hand and value
        print("Your current value is Blackjack! (21)" if player_hand['value'] == 21
              else f"Your current value is {player_hand['value']}.")
        print(f"With the hand: {formatted_hand(player_hand['cards'])}\n")
        
        action = int(input("Hit or stay? (Hit = 1, Stay = 0): "))
        
        # Player decides to hit
        if action == 1:
            hit = random.choice(deck)
            print(f"You draw {formatted_single_card(hit)}.")
            deck.remove(hit)
            player_hand['cards'].append(hit)
            player_hand['value'] = hand_value(player_hand['cards'])
            print()

            if player_hand['value'] == 21:
                print("Your current value is Blackjack! (21)")
            elif player_hand['value'] > 21:
                print("Your current value is bust! (>21)")
                player_busts = True
                break
        else:  # Player decides to stay
            break
    
    # Dealer's turn (only if player hasn't busted)
    while not player_busts:
        print(f"\nDealer's current value is {dealer_hand['value']}.")   
        print(f"With the hand: {formatted_hand(dealer_hand['cards'])}")
        
        # Dealer must hit until their hand's value is 17 or more
        while dealer_hand['value'] < 17:
            hit2 = random.choice(deck)
            print(f"\nDealer draw {formatted_single_card(hit2)}.")
            deck.remove(hit2)
            dealer_hand['cards'].append(hit2)
            dealer_hand['value'] = hand_value(dealer_hand['cards'])
            
            print()
            if dealer_hand['value'] == 21:
                print("Dealer's current value is Blackjack! (21)")
            elif dealer_hand['value'] > 21:
                print("Dealer's current value is Bust! (>21)")
            else:
                print(f"Dealer's current value is {dealer_hand['value']}.")
            print(f"With the hand: {formatted_hand(dealer_hand['cards'])}")
        break

def determine_winner(player_hand, dealer_hand):
    # Compare hands and declare the winner
    player_value = player_hand['value']
    dealer_value = dealer_hand['value']
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
    elif player_value > dealer_value:
        print("*** You beat the dealer! ***")
    else:  # player_value < dealer_value
        print("*** Dealer wins! ***")

def main():
    # Main game loop
    while True:
        # Initialize a new game
        deck = create_52cards()
        player_hand, dealer_hand, deck = initial_cards(deck)
        
        # Play the game
        game_logic(player_hand, dealer_hand, deck)
        determine_winner(player_hand, dealer_hand)
        
        # Ask if the player wants to play again
        while True:
            ask = input("Want to play again? (y/n): ").lower()
            if ask == 'y':
                print("-"*50)
                break
            elif ask == 'n':
                return  # Exit the game
            else:
                print("Invalid input! Try again. (y/n)")

# Run the Blackjack game
main()