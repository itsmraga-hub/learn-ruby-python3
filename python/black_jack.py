"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ['J', 'Q', 'K']:
      return 10
    elif card == 'A':
      return 1
    elif int(card) in range(1, 11, 1):
      return int(card)
    else:
      return card

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    card_one_result = value_of_card(card_one)
    card_two_result = value_of_card(card_two)
    # print(value_of_card(''))
    if card_one_result > card_two_result:
      return card_one
    elif card_one_result < card_two_result:
      return card_two
    else:
      return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one_result = value_of_card(card_one)
    card_two_result = value_of_card(card_two)
    total = card_one_result + card_two_result
    if card_one_result == 1 or card_two_result == 1:
      return 11
    elif 21 - total >= 11:
      return 11
    else:
      return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one_result = value_of_card(card_one)
    card_two_result = value_of_card(card_two)
    
    if card_one_result == 1:
      card_one_result = value_of_ace(card_one, card_two)
    if card_two_result == 1:
      card_two_result = value_of_ace(card_one, card_two)
    
    total = card_one_result + card_two_result

    if total == 21:
      return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_one_result = value_of_card(card_one)
    card_two_result = value_of_card(card_two)
    
    if card_one_result == card_two_result:
      return True
    return False

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    card_one_result = value_of_card(card_one)
    card_two_result = value_of_card(card_two)
    total = card_one_result + card_two_result

    if total == 9 or total == 10 or total == 11:
      return True
    return False

# print(higher_card('K', '10'))
# print(value_of_card(''))
print(value_of_ace('Q', 'A'))
print(value_of_ace('2', 'A'))
# print(is_blackjack('A', 'K'))
# print(is_blackjack('10', '9'))
# print(can_split_pairs('Q', 'K'))
# print(can_split_pairs('10', 'A'))
# print(can_double_down('A', '9'))
# print(can_double_down('10', '2'))