#!/usr/local/bin/python3
from random import randint, choice, seed
case_num = int(input())
# seed(999)
# 0 and 1 are the sample cases
maze0 ='''
#####...####
###...####..
#####.#.####

############
#.....######
#####...####'''.lstrip()

maze1 = '''
########..
####.#####
##########
#.####.###

......####
..........
..........
..........'''.lstrip()
if case_num == 0:
    print(12, 3)
    print(maze0)
elif case_num == 1:
    print(10, 4)
    print(maze1)
else:
    # output what should be read in as input by
    # contestant code
    x = randint(3, 200)
    y = randint(3, 200)
    print(x, y)
    for _ in range(y):
        print("".join(choice(["#", "."]) for _ in range(x)))
    print()
    for _ in range(y):
        print("".join(choice(["#", "."]) for _ in range(x)))
