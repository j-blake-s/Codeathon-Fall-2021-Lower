
import random

TOZAN = "T"
SEPPO = "S"
EMPTY = "~"
fpath = "C:/Users/Blake/Desktop/Github/Codeathon-Fall-2021-Lower/TheMonkGame/sample.txt"

def helper(tile,token):
    if tile == token: return 1
    if tile == EMPTY: return 0
    else: return None


def rand_help():

    e = random.randint(-1,1)
    if e == -1:
        return SEPPO
    if e == 1:
        return TOZAN
    if e == 0:
        return EMPTY

def rand_board(M,N):
    board = [[None] * N]*M
    board = [[rand_help() for e in row] for row in board]
    return board



    
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

        

def argmax(l:list):
    return l.index(min(l)) if abs(min(l)) > max(l) else l.index(max(l))

if __name__ == "__main__":
    #lines = open(fpath).readlines()
    #(M,N,K) = list(map(int,lines[0].split()))
    #board = list(map(str.split,lines[1:]))
    #print(solve(M,N,K,board))
    (M,N) = (15,15)
    #random.seed(0)
    board = rand_board(M,N)
    [print(row) for row in board]
    f = [solve(M,N,K,board) for K in range(3,min(M,N))]
    K = argmax(f)
    print(f)
    print(K)