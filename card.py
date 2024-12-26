from random import shuffle
from enum import Enum

from colours import blue, green, red, yellow


class Colour(Enum):
    BLUE = blue
    GREEN = green
    RED = red
    YELLOW = yellow


class ChangeDirectionCard:
    pass


class SkipCard:
    pass


class ReverseCard:
    pass


class ChangeColourCard:
    pass


class PickUpCard:

    def __init__(self, pickup_number: int) -> None:
        self.number = pickup_number
        self.pickup_number = f"+{pickup_number}"

    def __repr__(self) -> str:
        return f"{self.number}"


class ColouredCard:

    def __init__(self, colour: Colour, number: int) -> None:
        self.colour = colour
        self.number = number

    def __repr__(self) -> str:
        return f"{self.colour.value} {self.number}"


class Deck:

    def __init__(self, decks: int = 1) -> None:
        self.cards = []
        self.dead_pile = []
        for _ in range(decks):
            for colour in Colour:
                for number in range(1, 10):
                    self.cards.append(ColouredCard(colour, number))

    def print_deck(self) -> None:
        for card in self.cards:
            print(card)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def next_card(self) -> ColouredCard:
        return self.cards.pop()

    def add_to_dead_pile(self, card: ColouredCard) -> None:
        self.dead_pile.append(card)


d = Deck()
d.shuffle()
d.print_deck()
a = 1
