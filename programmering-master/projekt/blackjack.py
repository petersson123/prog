
import random

# Skapa en kortlek med fyra kort av varje valör (1-13)
deck = [i for i in range(1, 14)] * 4

# Funktion för att blanda kortleken
def shuffle_deck():
    random.shuffle(deck)

# Funktion för att dra ett kort från leken
def draw_card():
    return deck.pop()

# Funktion för att beräkna summan av en hand
def hand_value(hand):
    value = 0
    num_aces = 0

    # Räkna varje kort i handen
    for card in hand:
        if card == 1:  # Ess
            num_aces += 1
            value += 11  # Lägg till 11 för tillfället
        elif card >= 11 and card <= 13:  # Knekt, Dam, Kung
            value += 10
        else:
            value += card

    # Justera essens värde beroende på handens totala värde
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

# Funktion för att spela spelet
def play_game():
    # Blanda kortleken
    shuffle_deck()

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
                return -1
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
        return -1
    elif computer_score > 21:
        return 1
    elif player_score > computer_score:
        return 1
    elif player_score < computer_score:
        return -1
    else:
        return 0

# Huvudprogrammet
def main():
    print("Välkommen till 21-spelet!")

    while True:
        result = play_game()

        if result == 1:
            print("Grattis, du vann!")
        elif result == -1:
            print("Tyvärr, du förlorade.")
        else:
            print("Det blev oavgjort.")

        play_again = input("Vill du spela igen? (ja/nej) ").lower()
        if play_again != "ja":
            break

    print("Tack för att du spelade!")

if __name__ == "__main__":
    main()


