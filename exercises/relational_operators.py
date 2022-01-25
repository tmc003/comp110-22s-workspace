"""Exercise 01."""

__author__ = "730316240"

left_hand_side = int(input("Pick a number."))
right_hand_side = int(input("Pick a number."))

less = left_hand_side < right_hand_side
greater = left_hand_side >= right_hand_side
equal = left_hand_side == right_hand_side
unequal = left_hand_side != right_hand_side

less_print = print(left_hand_side, " < ",  right_hand_side,  " is ", less)
greater_print = print(left_hand_side, " >= ", right_hand_side, " is ", greater)
equal_print = print(left_hand_side, " == ", right_hand_side, " is ", equal)
unequal_print = print(left_hand_side, " != ",  right_hand_side, " is ", unequal)
