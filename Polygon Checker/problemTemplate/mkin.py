#!/usr/local/bin/python3
# from random import randint, choices, choice
import random
import string
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print('''4
A->B
B->C
C->D
D->A''')
elif case_num == 1:
    print('''5
A->B
B->C
C->D
D->A
C->A''')
else:
    # output what should be read in as input by
    # contestant code
    n = random.randint(3, 10000)
    print(n)
    will_work = random.choice([True, False])
    points = set()
    while len(points) < n:
        points.add("".join(random.choices(string.ascii_letters, k=random.randint(1,5))))
    points = list(points)
    if will_work:
        lines = [f"{points[i]}->{points[(i+1)%n]}" for i in range(n)]
    else:
        lines = [f"{points[i]}->{points[(i//2*4)%n]}" for i in range(n)]

    random.shuffle(lines)
    print("\n".join(lines))
    # j = random.randint(3, 2 ** 25)
    # print(n, j)
