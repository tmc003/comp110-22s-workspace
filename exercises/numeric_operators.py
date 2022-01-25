"""Exercise 01."""

__author__ = "730316240"

left_hand_side = int(input("Pick a number 1 - 10 "))
right_hand_side = int(input("Pick a number 1 - 10 "))

exponential = left_hand_side ** right_hand_side
division = left_hand_side / right_hand_side
integerD = left_hand_side // right_hand_side
remainder = left_hand_side % right_hand_side

exponential_print = print(left_hand_side, " ** ", right_hand_side, " is ", exponential)
division_print = print(left_hand_side, " / ", right_hand_side, " is ", division) 
integerD_print = print(left_hand_side, " // ", right_hand_side, " is ", integerD) 
remainder_print = print(left_hand_side, " % ", right_hand_side, " is ", remainder)
