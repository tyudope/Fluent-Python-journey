import collections

Card = collections.namedtuple("Card", ["rank","suit"])

class FrenchDeck:

    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()


    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]


    def __len__(self):
        return len(self._cards)


    def __getitem__(self, position):
        return self._cards[position]




deck = FrenchDeck()
print(len(deck))


# Reading specific cards from the deck say, the first or the last is easy, thanks to the __getitem__ method.
print(f"First card in the deck {deck[0]}")
print(f"Last card in the deck {deck[-1]}")


# Should we create a method to a pick a random card ? No needed. Python already has a function to get a random item
# from a sequence : random.choice We can use it on a deck instance.

from random import choice
print("Random card : ",choice(deck))

# __getitem__ delegates to the [] operator, that's why it's support slicing.
print(deck[:5])


#just by implementing the __getitem__ special method, our deck is also iterable.

for card in deck:
    print(card, end=" ")


print("")
print(Card("Q", "hearts") in deck)
print(Card("7", "beasts") in deck)



# how about sorting
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key = spades_high):
    print(card, end = " ")

print("")


