from card import Card
from deck import Deck

# ==============
# = CARD TESTS =
# ==============

def test_card_valid_match_1():
    card1 = Card("rectangle", 1, "red", "empty")
    card2 = Card("rectangle", 1, "red", "hatched")
    card3 = Card("rectangle", 1, "red", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_2():
    card1 = Card("rectangle", 1, "red", "empty")
    card2 = Card("rectangle", 1, "green", "empty")
    card3 = Card("rectangle", 1, "blue", "empty")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_3():
    card1 = Card("rectangle", 1, "red", "filled")
    card2 = Card("rectangle", 2, "red", "filled")
    card3 = Card("rectangle", 3, "red", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_4():
    card1 = Card("rectangle", 3, "blue", "hatched")
    card2 = Card("wave", 3, "blue", "hatched")
    card3 = Card("diamond", 3, "blue", "hatched")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_5():
    card1 = Card("rectangle", 1, "red", "empty")
    card2 = Card("rectangle", 1, "blue", "hatched")
    card3 = Card("rectangle", 1, "green", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_6():
    card1 = Card("rectangle", 1, "red", "empty")
    card2 = Card("diamond", 1, "red", "hatched")
    card3 = Card("wave", 1, "red", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_7():
    card1 = Card("rectangle", 1, "red", "empty")
    card2 = Card("rectangle", 3, "red", "hatched")
    card3 = Card("rectangle", 2, "red", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_8():
    card1 = Card("wave", 1, "blue", "hatched")
    card2 = Card("rectangle", 1, "red", "hatched")
    card3 = Card("diamond", 1, "green", "hatched")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_9():
    card1 = Card("diamond", 2, "red", "empty")
    card2 = Card("wave", 1, "red", "empty")
    card3 = Card("rectangle", 3, "red", "empty")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_10():
    card1 = Card("wave", 2, "blue", "empty")
    card2 = Card("wave", 3, "green", "empty")
    card3 = Card("wave", 1, "red", "empty")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_11():
    card1 = Card("rectangle", 1, "blue", "empty")
    card2 = Card("rectangle", 2, "green", "hatched")
    card3 = Card("rectangle", 3, "red", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_12():
    card1 = Card("rectangle", 3, "red", "empty")
    card2 = Card("wave", 3, "blue", "hatched")
    card3 = Card("diamond", 3, "green", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_13():
    card1 = Card("diamond", 1, "green", "empty")
    card2 = Card("wave", 2, "green", "hatched")
    card3 = Card("rectangle", 3, "green", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_14():
    card1 = Card("wave", 2, "red", "filled")
    card2 = Card("diamond", 3, "green", "filled")
    card3 = Card("rectangle", 1, "blue", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_valid_match_15():
    card1 = Card("rectangle", 2, "blue", "empty")
    card2 = Card("wave", 3, "red", "hatched")
    card3 = Card("diamond", 1, "green", "filled")
    assert card1.matches_with(card2, card3)
    assert card2.matches_with(card1, card3)
    assert card3.matches_with(card1, card2)

def test_card_invalid_match_1():
    card1 = Card("rectangle", 2, "red", "empty")
    card2 = Card("rectangle", 1, "blue", "empty")
    card3 = Card("rectangle", 1, "green", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_2():
    card1 = Card("rectangle", 2, "red", "empty")
    card2 = Card("wave", 3, "red", "empty")
    card3 = Card("rectangle", 1, "red", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_3():
    card1 = Card("rectangle", 1, "red", "empty")
    card2 = Card("wave", 1, "green", "empty")
    card3 = Card("diamond", 1, "red", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_4():
    card1 = Card("rectangle", 1, "green", "empty")
    card2 = Card("rectangle", 1, "red", "hatched")
    card3 = Card("rectangle", 1, "blue", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_5():
    card1 = Card("rectangle", 2, "red", "empty")
    card2 = Card("wave", 2, "red", "empty")
    card3 = Card("rectangle", 1, "red", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_6():
    card1 = Card("rectangle", 1, "blue", "empty")
    card2 = Card("rectangle", 1, "red", "empty")
    card3 = Card("diamond", 1, "red", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_7():
    card1 = Card("wave", 1, "red", "empty")
    card2 = Card("rectangle", 1, "red", "empty")
    card3 = Card("rectangle", 1, "red", "hatched")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_8():
    card1 = Card("wave", 1, "red", "empty")
    card2 = Card("rectangle", 2, "green", "empty")
    card3 = Card("diamond", 1, "red", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_9():
    card1 = Card("rectangle", 2, "red", "empty")
    card2 = Card("diamond", 2, "red", "empty")
    card3 = Card("wave", 3, "red", "filled")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_10():
    card1 = Card("rectangle", 1, "red", "empty")
    card2 = Card("rectangle", 1, "blue", "empty")
    card3 = Card("rectangle", 1, "red", "filled")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_11():
    card1 = Card("rectangle", 2, "red", "empty")
    card2 = Card("wave", 1, "red", "empty")
    card3 = Card("rectangle", 1, "blue", "empty")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_12():
    card1 = Card("wave", 3, "red", "hatched")
    card2 = Card("rectangle", 3, "red", "empty")
    card3 = Card("wave", 1, "red", "filled")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_13():
    card1 = Card("rectangle", 2, "blue", "hatched")
    card2 = Card("rectangle", 2, "red", "empty")
    card3 = Card("diamond", 2, "red", "hatched")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_14():
    card1 = Card("rectangle", 3, "green", "empty")
    card2 = Card("rectangle", 1, "red", "empty")
    card3 = Card("rectangle", 1, "red", "filled")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)

def test_card_invalid_match_15():
    card1 = Card("wave", 1, "red", "filled")
    card2 = Card("rectangle", 3, "green", "hatched")
    card3 = Card("rectangle", 1, "red", "hatched")
    assert not card1.matches_with(card2, card3)
    assert not card2.matches_with(card1, card3)
    assert not card3.matches_with(card1, card2)
