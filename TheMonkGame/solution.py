
import random

TOZAN = "T"
SEPPO = "S"
EMPTY = "~"

def solve(M,N,K,board):
    spots = 0
    #$ Vert Check
    for j in range(M-K+1):
        for i in range(N):
            try:
                if sum([helper(x[i],SEPPO) for x in board[j:K+j]]) == K-1: spots-=1
            except: pass
            try:
                if sum([helper(x[i],TOZAN) for x in board[j:K+j]]) == K-1: spots+=1
            except: pass

    #$ Zont Check
    for row in board:
        for i in range(N-K+1):
            try:
                if sum([helper(e,SEPPO) for e in row[i:i+K]])==K-1: spots-=1
            except: pass
            try:
                if sum([helper(e,TOZAN) for e in row[i:i+K]])==K-1: spots+=1
            except: pass

    #$ Right Diag Check
    for i in range(M-K+1):
        for j in range(N-K+1):
            try:
                if sum([helper(board[i+l][j+l],SEPPO) for l in range(K)])==K-1: spots-=1
            except: pass

            try:
                if sum([helper(board[i+l][j+l],TOZAN) for l in range(K)])==K-1: spots+=1
            except: pass

    #$ Left Diag Check
    for i in range(M-K+1):
        for j in range(N,K-1,-1):
            try:
                if sum([helper(board[i+l][j-l-1],SEPPO) for l in range(K)])==K-1: spots-=1
            except: pass

            try:
                if sum([helper(board[i+l][j-l-1],TOZAN) for l in range(K)])==K-1: spots+=1
            except: pass

    return spots

def helper(tile,token):
    if tile == token: return 1
    if tile == EMPTY: return 0
    else: return None



def stringBoard(board):
    board_str = "\n"
    for row in board:
        buffer = ""
        for e in row:
            board_str += buffer + e
            buffer = " "
        board_str += "\n"
    return board_str

if __name__ == "__main__":


    (M,N,K) = list(map(int,input().split()))

    board = []
    for _ in range(M):
        board.append(input().split())

    solve(M,N,K,board)
    print(stringBoard(board))