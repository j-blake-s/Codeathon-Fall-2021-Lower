x, y = map(int, input().split())
board1 = []
for _ in range(y):
    board1.append(input())
board2 = []
_ = input()
for _ in range(y):
    board2.append(input())

total = 0
for i in range(y):
    for j in range(x):
        total += board1[i][j] == "." and board2[i][j] == "."
print(total)