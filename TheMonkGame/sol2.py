from copy import deepcopy
m, n, k = map(int, input().split())

board = [input().split() for _ in range(m)]
assert all(len(board[i]) == n for i in range(m))

# print(board)

t_seen = set()
WIN_MARKER = "#"
BLANK = "~"
def count_wins(search_for):
    # horizontal wins
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x:x+k].count(search_for) == k - 1 and \
                board[y][x:x+k].count(BLANK) == 1:
                board[y][x:x+k] = [z if z == search_for else WIN_MARKER for z in board[y][x:x+k]]
    
    # vertical wins
    for x in range(len(board[0])):
        for y in range(len(board) - (k-1)):
            temp = [board[y+h][x] for h in range(k)]
            # print(temp)
            if temp.count(search_for) == k - 1 and \
                temp.count(BLANK) == 1:
                for h in range(k):
                    if board[y+h][x] == BLANK:
                        board[y+h][x] = WIN_MARKER

    # down and to the right diagonals
    for x in range(len(board[0])):
        for y in range(len(board)):
            try:
                temp = [board[y+h][x+h] for h in range(k)]
            except: 
                break
            if temp.count(search_for) == k - 1 and \
                temp.count(BLANK) == 1:
                for h in range(k):
                    if board[y+h][x+h] == BLANK:
                        board[y+h][x+h] = WIN_MARKER
    
    # up and to the right diagonals
    for x in range(len(board[0])):
        for y in range(len(board)):
            if y - (k-1) < 0 or x + (k-1) >= len(board[0]):
                continue
            temp = [board[y-h][x+h] for h in range(k)]
            # print(temp)
            if temp.count(search_for) == k - 1 and \
                temp.count(BLANK) == 1:
                for h in range(k):
                    if board[y-h][x+h] == BLANK:
                        board[y-h][x+h] = WIN_MARKER

    for line in board:
        print(*line, sep='')
    
    return sum(line.count(WIN_MARKER) for line in board)

og = deepcopy(board)
t_wins = (count_wins("T"))
print()
board = deepcopy(og)
s_wins = (count_wins("S"))
print(t_wins - s_wins)