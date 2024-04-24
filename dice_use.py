from dice_test import roll_dice
from unittest import mock
def guess_numer(num):
    result = roll_dice()
    if result == num:
        return "You won"
    else:
        return "You Lost!"
    
