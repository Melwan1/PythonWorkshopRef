from card import Card
import random

class Deck:
    
    def __init__(self):
        self.showed : list[Card] = []
        self.played : list[Card] = []
        self.hidden : list[Card] = []
        for color in ["red", "green", "blue"]:
            for shape in ["wave", "diamond", "rectangle"]:
                for number in range(1, 4):
                    for filling in ["empty", "hatched", "filled"]:
                        self.hidden.append(Card(shape, number, color, filling))
    
    def shuffle(self, seed : int = None):
        random.seed(seed)
        for step in range(81):
            index : int = random.randint(0, 80)
            self.hidden[index], self.hidden[step] = self.hidden[step], self.hidden[index]
        for card in self.hidden:
            print(card)
    
    def display_cards(self):
        number_cards_to_show = 0
        if len(self.showed) < 12:
            number_cards_to_show = 12 - len(self.showed)
        elif len(self.showed) > 15:
            number_cards_to_show = 0
        else:
            number_cards_to_show = 3
        if len(self.hidden) < number_cards_to_show:
            number_cards_to_show = len(self.hidden)
            # this ensures that if self.hidden is empty then the method does nothing
        for _ in range(number_cards_to_show):
            card : Card = self.hidden.pop(0)
            self.showed.append(card)
    
    def play_step(self) -> bool:
        for index1 in range(len(self.showed)):
            for index2 in range(index1 + 1, len(self.showed)):
                for index3 in range(index2 + 1, len(self.showed)):
                    if self.showed[index1].matches_with(self.showed[index2], self.showed[index3]):
                        # match!
                        card3 = self.showed.pop(index3)
                        card2 = self.showed.pop(index2)
                        card1 = self.showed.pop(index1)
                        print("Matched cards at indices", index1, index2, index3)
                        print(card1)
                        print(card2)
                        print(card3)
                        self.played.extend([card1, card2, card3])
                        if len(self.showed) < 12:
                            self.display_cards()
                        return True
                        
        # nothing has matched
        self.display_cards()
        return False
    
    def run_game(self):
        self.shuffle()
        play_step_result = True
        while play_step_result or len(self.hidden) > 0:
            play_step_result = self.play_step()
        for _ in range(3):
            self.play_step()
        print("Game over! Matched cards:", len(self.played))
        print("Remaining cards showed:")
        for card in self.showed:
            print(card)
    

deck = Deck()
deck.run_game()