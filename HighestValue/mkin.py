#!/usr/local/bin/python3
from random import randint, seed
case_num = int(input())
seed(64)
# 0 and 1 are the sample cases
if case_num == 0:
    print(1)
    print(5)
    print(1, 8, 2, 9, 2)
elif case_num == 1:
    print(2)
    print(7)
    print(156, 572, 12, 56, 9076, 789, 23)
    print(4)
    print(15, 57, 12, 60)
else:
    # output what should be read in as input by
    # contestant code
    t = randint(1, 20)
    print(t)
    for _ in range(t):
        n = randint(2, 1000)
        print(n)
        if case_num >= 40:
            print(*sorted([randint(1, 300000) for i in range(n)], reverse=True))
        else:
            print(*[randint(1, 300000) for i in range(n)])
    # j = randint(3, 2 ** 25)
    # print(n, j)
