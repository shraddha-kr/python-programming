#A deck as a sequence of Cards, a class to represent a deck of playing cards
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # 13 X 4 = 52
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]  

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(deck.__dict__)
print(len(deck))

print(FrenchDeck.ranks)