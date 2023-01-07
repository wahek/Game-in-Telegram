import random
import commands

total = 150

def get_total():
    global total
    return total

def set_total(value):
    global total
    total = value
    return total

def choice():
    choice = random.randint(1, 2)
    if choice == 1:
        return choice
    else:
        return choice

def candies_play_bot_random():
    global total
    cech = random.randint(1, 28)
    total -= cech
    return cech


def candies_play_user(candies):
    global total
    total -= int(candies)
    return total

def candies_bot_win():
    global total
    count = 0
    while total != 29:
        count += 1
        total -= 1
    return count