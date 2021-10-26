#!/usr/local/bin/python3
from random import randint
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    # print(4, 2)
    print(3)
    print(1, 2, 3)
elif case_num == 1:
    print(4)
    print(1, 2, 3, 4)
elif case_num == 2:
    print(5)
    print(50, 10011, 13003, 20, 2)
else:
    # output what should be read in as input by
    # contestant code
    n = randint(3, 100000)
    print(n)
    print(*[randint(0, 9) for _ in range(n)])

    # j = randint(3, 2 ** 25)
    # print(n, j)
