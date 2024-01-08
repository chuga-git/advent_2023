from collections import Counter
import copy

in_path = 'day7.in'

with open(in_path) as f_in:
    lines = f_in.read().splitlines()

RANKS = { 'A': 41, 'K': 37, 'Q': 31, 'J': 29, 'T': 23, '9': 19, '8': 17, '7': 13, '6': 11, '5': 7, '4': 5, '3': 3, '2': 2 }
RANKS_2 = { 'A': 37, 'K': 31, 'Q': 29, 'T': 23, '9': 19, '8': 17, '7': 13, '6': 11, '5': 7, '4': 5, '3': 3, '2': 2, 'J': 1 }

# i don't know how enums work
FIVE_KIND = 7
FOUR_KIND = 6
FULL_HOUSE = 5
THREE_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

class Hand:
    def __init__(self, cards, bid, hand_type) -> None:
        self.cards = cards
        self.bid = bid
        self.hand_type = hand_type

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        else:
            for i in range(len(self.cards)):
                if self.cards[i] < other.cards[i]:
                    return True
                if self.cards[i] > other.cards[i]:
                    return False

def parse_hands(text):
    hands = []

    for line in text:
        card_str, bid = line.split()

        cards = [RANKS[x] for x in card_str]

        hand_type = eval_type(cards)

        hands.append(Hand(cards, int(bid), hand_type))
    
    return hands

def parse_hands_2(text):
    hands = []

    for line in text:
        card_str, bid = line.split()

        cards = [RANKS_2[x] for x in card_str]
        hand_type = eval_type_2(copy.deepcopy(cards))
        hands.append(Hand(cards, int(bid), hand_type))
    
    return hands

# if i don't understand object mutability, then it can't hurt me
def convert_jokers(hand):
    if 1 in hand:
        count = Counter(hand)
        if len(count) == 1:
            return hand
        count.pop(1)
        convert_to = count.most_common()[0][0]

        for i in range(len(hand)):
            if hand[i] == 1:
                hand[i] = convert_to

    return hand

def eval_type(hand):
    common = Counter(hand).most_common(5)

    if len(common) == 1:
        return FIVE_KIND
    
    if len(common) == 2:
        if common[0][1] == 4:
            return FOUR_KIND
        return FULL_HOUSE
        
    if len(common) == 3:
        if common[0][1] == 3:
            return THREE_KIND
        return TWO_PAIR
        
    if len(common) == 4:
        return ONE_PAIR
    
    return HIGH_CARD

def eval_type_2(hand):
    return eval_type(convert_jokers(hand))

def part1():
    hands_sort = sorted(parse_hands(lines))
    winnings = 0

    for i in range(len(hands_sort)):
        winnings += (hands_sort[i].bid * (i + 1))
    
    return winnings

def part2():
    hands_sort = sorted(parse_hands_2(lines))
    for p in hands_sort:
        print(f'{p.cards} {p.hand_type}')
    winnings = 0

    for i in range(len(hands_sort)):
        winnings += (hands_sort[i].bid * (i + 1))
    
    return winnings

print(part1())
print(part2())