# Gra karciana
# W grze znajduje się talia kart, a każda karta ma określoną wartość. W każdej rundzie obaj gracze otrzymują po jednej karcie. Następnie wartości kart są porównywane, a gracz posiadający kartę o większej wartości otrzymuje punkt.Gra składa się z 5 rund.
# W każdej rundzie:
# Gracz 1 otrzymuje jedną kartę.
# Gracz 2 otrzymuje jedną kartę.
# Program wyświetla karty otrzymane przez obu graczy.
# Program porównuje wartości kart.
# Gracz posiadający kartę o większej wartości otrzymuje jeden punkt.
# Jeżeli obaj gracze otrzymają karty o takiej samej wartości, runda kończy się remisem i żaden z graczy nie otrzymuje punktu.
# Po każdej rundzie program powinien wyświetlić aktualny wynik obu graczy.
# Po zakończeniu wszystkich 5 rund program powinien wyświetlić końcowy wynik oraz informację o tym, który gracz wygrał. Jeżeli obaj gracze mają taką samą liczbę punktów, program powinien poinformować o remisie.
# Dodatkowe wymaganie
# Karty powinny być rozdawane w sposób losowy. W tym celu można wykorzystać zewnętrzną bibliotekę random oraz jej funkcje związane z losowaniem i mieszaniem elementów.
# Pamiętaj, że karta po rozdaniu nie może pozostać w talii, ponieważ nie może zostać rozdana ponownie.

import random
from reusable_functions import get_deck_of_cards

player_1_points = 0
player_2_points = 0

cards = get_deck_of_cards()

# shuffle
cards_list = list(cards)
random.shuffle(cards_list)  # działa tylko na listach
print(cards_list)

# program
for i in range(5):
    # losowanie karty dla playera 1
    # wylosowana karta, jej wartość i usunięcie z talii

    drawn_card = cards_list.pop()
    print(f"Gracz player1 wylosował: {drawn_card}, kartę usunięto z talii")
    drawn_card_value = cards.get(drawn_card)

    # losowanie karty dla playera 2
    drawn_card_2 = cards_list.pop()
    print(f"Gracz player2 wylosował: {drawn_card_2}, kartę usunięto z talii")
    drawn_card_value_2 = cards.get(drawn_card_2)

    # dystrybucja punktów
    if drawn_card_value > drawn_card_value_2:
        player_1_points += 1
    elif drawn_card_value_2 > drawn_card_value:
        player_2_points += 1
    else:
        print("Remis")

    # ogłoszenie statusu punktów po rundzie
    print(
        f"Status punktów po rundzie {i+1} - gracz 1 : {player_1_points} pkt, gracz 2: {player_2_points} pkt")
    print("-------------------------------------------------------------")


# Wynik końcowy
print(
    f"Wynik końcowy - Gracz 1: {player_1_points} pkt, gracz 2: {player_2_points} pkt")
if player_1_points > player_2_points:
    print("Gracz 1 wygrywa!")
elif player_2_points > player_1_points:
    print("Gracz 2 wygrywa!")
else:
    print('Remis')
