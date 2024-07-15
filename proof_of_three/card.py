class Card:
    def __init__(self, shape : str, number : int, color : str, filling : str):
        self.shape = shape
        self.number = number
        self.color = color
        self.filling = filling
    
    def match_characteristic(self, char1, char2, char3):
        if char1 == char2 and char2 == char3:
            return True
        if char1 == char2:
            return False
        if char2 == char3:
            return False
        if char1 == char3:
            return False
        return True
    
    def matches_with(self, card2: "Card", card3 : "Card") -> bool:
        return self.match_characteristic(self.shape, card2.shape, card3.shape) \
            and self.match_characteristic(self.number, card2.number, card3.number) \
            and self.match_characteristic(self.color, card2.color, card3.color) \
            and self.match_characteristic(self.filling, card2.filling, card3.filling)
    
    def __repr__(self):
        return f"Card({self.color}, {self.shape}, {self.number}, {self.filling})"