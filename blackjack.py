import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal_card():
    return random.choice(cards)



def calculate_score(hand):

    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)



def compare(player_score, dealer_score):
    if player_score > 21:
        return "You went over 21! You lose."
    elif dealer_score > 21:
        return "Dealer went over 21! You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins!"



def play_blackjack():
    # Initial hands for player and dealer
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False


    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your hand: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 21:
            print("Blackjack! You win!")
            return
        elif player_score > 21:
            game_over = True
            break

       
        option = input("Type 'hit' to get another card or 'stand' to hold your current hand: ").lower()

        if option == 'hit':
            player_hand.append(deal_card())
        elif option == 'stand':
            game_over = True
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")

   
    while dealer_score != 21 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

   
    print(f"\nYour final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

    # Determine the winner
    print(compare(player_score, dealer_score))



play_blackjack()