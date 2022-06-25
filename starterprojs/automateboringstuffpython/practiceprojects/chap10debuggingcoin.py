import random
import logging

guess = 123;

while guess not in (0, 1):
    print('guess coin toss, enter heads or tails: ')
    guess = input()
    toss = random.randint(0,1) # 0 is tail, 1 is head
    print(toss)
    if toss == int(guess):
        print('you got it')
    else:
        print('nope, guess again')
    # guess = input()
    # if toss == guess:
    #     print('you got it')
    # else:
    #     print('nope, you are really bad shape')
