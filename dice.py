'''
ThunderRoad Dice Simulator

There are 7 dices in the game ThunderRoad:

o 3 red dice are active players dice
o 3 yellow dice are defense rolls
o 1 black "road" Bonus Dice
* Modify the dice generator to match this sequence
* 1=1
* 2=1
* 3=1
* 4=2
* 5=2
* 6=3
'''
from random import randint
from sys import exit
import os


def handle_roll(total_counts):
    die1, die2 = randint(1, 6), randint(1, 6)
    total = die1 + die2
    total_counts[total - 2] += 1

    print 'Die 1: %d \nDie 2: %d \nTotal: %d' % (die1, die2, total)
    print '\n\nRoll again?'
    response = raw_input('Press enter to roll again, type "stats" to view scores, or "quit" to exit.\n> ').lower()
    if response == '':
        return handle_roll
    elif response == 'stats':
        return handle_stats
    elif response == 'quit':
        return None

    return handle_unknown


def handle_stats(total_counts):
    for i in xrange(0, 11):
        print '%ds: %d' % (i + 2, total_counts[i])
    raw_input('')
    return handle_roll


def handle_unknown(total_counts):
    print 'I don\'t know what that means so you get to roll again.'
    raw_input('')
    return handle_roll


def main():
    os.system('clear')
    print 'Welcome to the dice rolling simulator!'
    raw_input('Press enter to begin.')

    total_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    state = handle_roll
    while state != None:
        os.system('clear')
        state = state(total_counts)


if __name__ == "__main__":
    main()
