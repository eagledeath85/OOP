import random


class Deck:
    PLAYING_CARDS = 52
    valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['H', 'D', 'C', 'S']

    def __init__(self):
        self.cards = [f'{value}{suit}' for suit in Deck.valid_suits for value in Deck.valid_values]

    def get_cards(self):
        return self.cards[:]

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]  # make a deep copy of cards
        return new_deck

    def sort_by_suit(self):
        cards_by_suits = {"H": [], "D": [], "C": [], "S": []}
        for card in self.cards:
            suit = self.cards[-1]
            cards_by_suits[suit].append(card)

        self.cards = (cards_by_suits["H"] + cards_by_suits["D"] + cards_by_suits["C"] + cards_by_suits["S"])

    def __len__(self):
        return len(self.get_cards())

    @staticmethod
    def shuffle(cards: list):
        random.shuffle(cards)

    def deal(self, n: int):
        dealt_cards = []

        for i in range(n):
            if len(self.cards) == 0:
                break
            card = self.cards.pop()
            dealt_cards.append(card)

        return dealt_cards

    def contains(self, card):
        return card in self.cards



d = Deck()
print(len(d))
cards = d.get_cards()
print(cards)
d.shuffle(cards)
print(cards)
print(d.deal(3))
print(d.contains('QS'))
print(len(d))