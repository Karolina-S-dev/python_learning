import random


def get_deck_of_cards():
    cards = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'walet', 'dama', 'król', 'as']
    colours = ['kier', 'karo', 'trefl', 'pik']
    # talia kart
    deck_of_cards = []
    for colour in colours:
        for card in cards:
            deck_of_cards.append(card + " " + colour)
    cards_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    cards_values_all = cards_values * 4
    # finalna talia z wartościami
    deck_with_values = dict(zip(deck_of_cards, cards_values_all))
    return deck_with_values


def get_drawn_card_and_delete(player, cards):
    drawn_card = random.choice(list(cards))
    print(f"Gracz {player} wylosował: {drawn_card}")
    # tutaj moznaby sie pozbyc 53 i 54
    drawn_card_value = cards.get(drawn_card)
    print(drawn_card_value)
    deleted_card = cards.pop(drawn_card, None)
    print(f"Z talii usunięto: {deleted_card}")
    print(cards)
    return drawn_card_value
