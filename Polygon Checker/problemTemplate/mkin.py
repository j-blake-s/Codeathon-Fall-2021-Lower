#!/usr/local/bin/python3
# from random import randint, choices, choice
import random
import string
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print('''2
4
A B
B C
C D
D A
3
BowL Dog
Dog WATER
Dog FOOd
''')
elif case_num == 1:
    print('''1
5
A B
B C
C D
D A
C A''')
else:
    # output what should be read in as input by
    # contestant code
    cases = random.randint(6, 8)
    if case_num == 40:
        cases = 20
    print(cases)
    for _ in range(cases):
        n = random.randint(5, 4999)
        if case_num == 40:
            n = 4900
        will_work = random.choice([True, False])
        points = set()
        while len(points) < n:
            points.add("".join(random.choices(string.ascii_letters, k=random.randint(1,5))))
        points = list(points)

        lines = [f"{points[i]} {points[(i+1)%n]}" for i in range(n)]
        if not will_work:
            x = random.randint(2, n-2)
            lines.append(f"{points[n-1]} {points[(n-1+x)%n]}")
            n += 1

        random.shuffle(lines)
        print(n)
        print("\n".join(lines))


    # else:
        # lines = [f"{points[i]} {points[(i//2*2+2)%n]}" for i in range(n)]

    # j = random.randint(3, 2 ** 25)
    # print(n, j)
