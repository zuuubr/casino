from random import choice


class GameBlackJack:
    def __init__(self, deposit):
        self.deposit = deposit

        self.diller_cards = []
        self.player_cards = []

        self.diller_score = 0
        self.player_score = 0

        self.cards = {"♠️2": 2, "♥️2": 2, "♣️2": 2, "♦️2": 2,
                      "♠️3": 3, "♥️3": 3, "♣️3": 3, "♦️3": 3,
                      "♠️4": 4, "♥️4": 4, "♣️4": 4, "♦️4": 4,
                      "♠️5": 5, "♥️5": 5, "♣️5": 5, "♦️5": 5,
                      "♠️6": 6, "♥️️6": 6, "♣️6": 6, "♦️6": 6,
                      "♠️7": 7, "♥️7": 7, "♣️7": 7, "♦️7": 7,
                      "♠️8": 8, "♥️8": 8, "♣️8": 8, "♦️8": 8,
                      "♠️9": 9, "♥️9": 9, "♣️9": 9, "♦️9": 9,
                      "♠️10": 10, "♥️10": 10, "♣️10": 10, "♦️10": 10,
                      "♠️J": 10, "♥️J": 10, "♣️J": 10, "♦️J": 10,
                      "♠️Q": 10, "♥️Q": 10, "♣️Q": 10, "♦️Q": 10,
                      "♠️K": 10, "♥️K": 10, "♣️K": 10, "♦️K": 10,
                      "♠️T": 11, "♥️T": 11, "♣️T": 11, "♦️T": 11}

    def get_card(self):
        card = choice(list(self.cards.items()))
        del self.cards[card[0]]

        return card
