import random

# Spelarens pengar
player_money = 100

# Skapa en kortlek med fyra kort av varje valör (1-13)
deck = [i for i in range(1, 14)] * 4

# Kartan som motsvarar numeriska värden
card_names = {
    1: 'E',
    11: 'J',
    12: 'Q',
    13: 'K'
}

# Funktion för att blanda kortleken
def shuffle_deck():
    random.shuffle(deck)

# Funktion för att dra ett kort från leken
def draw_card():
    card = deck.pop()
    return card_names.get(card, card)

# Funktion för att beräkna summan av en hand
def hand_value(hand):
    value = 0
    num_aces = 0

    # Räkna varje kort i handen
    for card in hand:
        if card == 'E':  # Ess
            num_aces += 1
            value += 11  # Lägg till 11 för tillfället
        elif card in ['J', 'Q', 'K']:  # Knekt, Dam, Kung
            value += 10
        else:
            value += card

    # Justera essens värde beroende på handens totala värde
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

# Funktion för att hantera insatser
def place_bet():
    global player_money
    while True:
        try:
            bet = int(input(f"Du har {player_money} kr. Ange din insats: "))
            if bet < 1 or bet > player_money:
                print("Ogiltig insats. Försök igen.")
            else:
                player_money -= bet
                return bet
        except ValueError:
            print("Ogiltigt värde. Försök igen.")

# Funktion för att spela spelet
def play_game():
    # Blanda kortleken
    shuffle_deck()

    # Placera insats
    bet = place_bet()

    # Spelarens hand
    player_hand = [draw_card(), draw_card()]
    print("Dina kort:", player_hand)

    # Datorns hand
    computer_hand = [draw_card()]
    print("Datorns kort:", computer_hand)

    # Spelarens tur att dra kort eller stanna
    while True:
        action = input("Vill du ta ett till kort (hit) eller stanna (stand)? ").lower()
        if action == "hit":
            player_hand.append(draw_card())
            print("Dina kort:", player_hand)
            if hand_value(player_hand) > 21:
                print("Du är tjock! Du förlorar.")
                return -bet
        elif action == "stand":
            break
        else:
            print("Ogiltigt val. Försök igen.")

    # Datorns tur att dra kort
    while hand_value(computer_hand) < 17:
        computer_hand.append(draw_card())
        print("Datorns kort:", computer_hand)

    # Jämför summan av händerna
    player_score = hand_value(player_hand)
    computer_score = hand_value(computer_hand)

    print("Din summa:", player_score)
    print("Datorns summa:", computer_score)

    if player_score > 21:
        return -bet
    elif computer_score > 21:
        return bet * 2
    elif player_score > computer_score:
        return bet * 2
    elif player_score < computer_score:
        return -bet
    else:
        return 0

# Huvudprogrammet
def main():
    global player_money
    print("Välkommen till 21-spelet!")

    while player_money > 0:
        result = play_game()

        if result > 0:
            player_money += result
            print(f"Grattis, du vann! Du har nu {player_money} kr.")
        elif result < 0:
            print(f"Tyvärr, du förlorade. Du har nu {player_money} kr.")
        else:
            print(f"Det blev oavgjort. Du har fortfarande {player_money} kr.")

        play_again = input("Vill du spela igen? (ja/nej) ").lower()
        if play_again != "ja":
            break

    print("Tack för att du spelade!")

if __name__ == "__main__":
    main()
