
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Return a random card"""
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose, Computer Blackjack"
    elif user_score == 0:
        return "Blackjack You Win!"
    elif user_score > 21:
        return "Bust. You Lose"
    elif computer_score > 21:
        return "You win, computer bust"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def blackjack():
    computer_cards = []
    user_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Computer card [{computer_cards[0]}, X]")
        print(f"Your card {user_cards} Your score {user_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            compare(user_score, computer_score)

        else:
            next_move = input("Do you want to hit or stand?\n")
            if next_move == "hit":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        print(f"Computer card {computer_cards} computer_score {computer_score}")
        print(f"Your card {user_cards} Your score {user_score}")
        print(compare(user_score, computer_score))


while input("Do you want to play blackjack? y or n: ") == "y":
    blackjack()


