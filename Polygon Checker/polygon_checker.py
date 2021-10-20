
import random


def solve():
    n = int(input())
    d = dict()
    for i in range(0, n):
        a, b = input().split("->")
        d[a] = 1 + (d[a] if a in d.keys() else 0)
        d[b] = 1 + (d[b] if b in d.keys() else 0)
        if (d[a] == 3 or d[b] == 3):
            print("False")
            break
    else:
        print("True" if 1 not in d.values() else "False")


def solve(inList):
    n = inList[0]
    d = dict()
    for i in range(1, n+1):
        a, b = inList[i].split("->")
        d[a] = 1 + (d[a] if a in d.keys() else 0)
        d[b] = 1 + (d[b] if b in d.keys() else 0)
        if (d[a] == 3 or d[b] == 3):
            return False
    else:
        return ("True" if 1 not in d.values() else "False")


def generateTest(solution, n):
    l = list()
    inputList = [n]
    for i in range(0, n):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
        a = ''.join(random.choice(letters)
                    for i in range(random.choice(range(1, 5))))
        while a in l:
            a = ''.join(random.choice(letters)
                        for i in range(random.choice(range(1, 5))))
        l.append(a)
    if solution:
        for i in range(-1, len(l)-1):
            if random.choice([True, False]):
                inputList.append(l[i]+"->"+l[i+1])
            else:
                inputList.append(l[i+1]+"->"+l[i])
        for i in range(0, len(inputList)):
            r1 = random.choice(range(1, n))
            r2 = random.choice(range(1, n))
            inputList[r1], inputList[r2] = inputList[r2], inputList[r1]
    else:
        if random.choice([True, False]):
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
            a = ''.join(random.choice(letters)
                        for i in range(random.choice(range(1, 5))))
            while a in l:
                a = ''.join(random.choice(letters)
                            for i in range(random.choice(range(1, 5))))
            l.append(a)
            for i in range(0, len(l)-1):
                if random.choice([True, False]):
                    inputList.append(l[i]+"->"+l[i+1])
                else:
                    inputList.append(l[i+1]+"->"+l[i])
            for i in range(0, len(inputList)):
                r1 = random.choice(range(1, n))
                r2 = random.choice(range(1, n))
                inputList[r1], inputList[r2] = inputList[r2], inputList[r1]
        else:
            for i in range(0, random.choice(range(1, len(l)//2))):
                l.pop(i)
            for i in range(0, len(l)):
                if random.choice([True, False]):
                    inputList.append(l[i]+"->"+random.choice(l))
                else:
                    inputList.append(random.choice(l)+"->"+l[i])
    return inputList


for i in range(0, 20):
    f = open("input/input"+("0"if i < 10 else "")+str(i)+".txt", "w+")
    a = generateTest(random.choice([True, False]),
                     random.choice(range(3, 10000)))
    for e in a:
        f.write(str(e)+"\n")
    f.close()
    f = open("output/output"+("0"if i < 10 else "") + str(i) + ".txt", "w+")
    f.write(str(solve(a)))
    f.close()
