import random 


class Player:
    def __init__(self,name,cards): #cards is list[Card]
        self.name = name
        self.cards = cards

    def first_card(self):
        return self.cards.pop(0)

    def add_card(self,card_a,card_b=None):
        self.cards.append(card_a)
        if card_b is not None:
            self.cards.append(card_b)
    def len_cards(self):
        return len(self.cards)


