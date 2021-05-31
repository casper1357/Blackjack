#Blackjack
import random

deck = {
    'Spades': {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Sixe': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10},
    'Diamonds': {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Sixe': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10},
    'Hearts': {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Sixe': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10},
    'Clubs': {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Sixe': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
}

#Getting players
players = int(input("Players?"))
player_points = [[] for i in range(players)]

#Player
for i in range(players):
    while sum(player_points[i]) < 21:
        if len(player_points[i]) == 0:
            print("--------------------------------")
            print(f"Player {i+1}")
            print(f"Automatically drew:")
            for x in range(2):
                suit = random.choice(list(deck))
                value = random.choice(list(deck[suit]))
                int_value = deck[suit][value]
                deck[suit].pop(value)
                print(f"{value} of {suit}")
                if int_value == 1:
                    if sum(player_points[i]) + 11 == 21:
                        player_points[i].append(11)
                    elif sum(player_points[i]) + 11 <= 21:
                        ace_p = int(input("1 or 11 from the ace?"))
                        player_points[i].append(ace_p)
                    else:
                        player_points[i].append(int_value)
                else:
                    player_points[i].append(int_value)
            print(f"Player {i + 1} has {player_points[i]}, a total of {sum(player_points[i])}")
        if len(player_points[i]) >= 5:
            print(f"Player {i+1} now has 5 cards")
            break
        action = input("Do you want to stay or hit?").lower()
        if action == "stay":
            print(f"Player {i+1} stopped at {sum(player_points[i])}")
            break
        if action == "hit":
            suit = random.choice(list(deck))
            value = random.choice(list(deck[suit]))
            int_value = deck[suit][value]
            deck[suit].pop(value)
            print(f"{value} of {suit}")
            if int_value == 1:
                if sum(player_points[i]) + 11 == 21:
                    player_points[i].append(11)
                if sum(player_points[i]) + 11 <= 21:
                    ace_p = int(input("1 or 11 from the ace?"))
                    player_points[i].append(ace_p)
                else:
                    player_points[i].append(int_value)
            else:
                player_points[i].append(int_value)
            print(f"Player {i + 1} has {player_points[i]}, a total of {sum(player_points[i])}")
total = 0
for i in range(players):
    if sum(player_points[i]) > 21:
        total += 21
    else:
        total += sum(player_points[i])
if total/len(player_points) > 21:
    print("Everybody lost")
else:
    # Dealer
    d_points = []
    won = False
    print("--------------------------------")
    while sum(d_points) < 17:
        for i in range(players):
            biggest = sum(player_points[0])
            if sum(player_points[i]) > biggest and sum(player_points[i]) <= 21:
                biggest = sum(player_points[i])
        if sum(d_points) > biggest:
            print("The dealer has won")
            won = True
            break
        suit = random.choice(list(deck))
        value = random.choice(list(deck[suit]))
        int_value = deck[suit][value]
        deck[suit].pop(value)
        if int_value == 1:
            if sum(d_points) + 11 >= 21:
                d_points.append(int_value)
            else:
                d_points.append(11)
        else:
            d_points.append(int_value)
        print(f"Dealer drew {value} of {suit}, a total of {sum(d_points)}")

    if won == False:
        if sum(d_points) > 21:
            for i in range(players):
                if sum(player_points[i]) <= 21:
                    print(f"Player {i+1} won")
                elif sum(player_points[i]) > 21:
                    print(f"Player {i+1} lost")
        else:
            for i in range(players):
                if len(player_points[i]) == 5 or sum(player_points[i]) > sum(d_points) and sum(player_points[i]) <= 21:
                    print(f"Player {i+1} won")
                elif sum(d_points) > sum(player_points[i]) or sum(player_points[i]) > 21:
                    print(f"Player {i+1} lost")
                elif sum(d_points) == sum(player_points[i]):
                    print(f"Split")