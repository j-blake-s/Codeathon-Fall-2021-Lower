x, y = map(int, input().split())
board1 = [input() for _ in range(y)]
_ = input()
board2 = [input() for _ in range(y)]
total = 0
for i in range(y):
    for j in range(x):
        total += board1[i][j] == "." and board2[i][j] == "."
print(total)