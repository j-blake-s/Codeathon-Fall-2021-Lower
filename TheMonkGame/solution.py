
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

def rand_help():
    e = random.randint(-1,1)
    if e == -1:
        return SEPPO
    if e == 1:
        return TOZAN
    if e == 0:
        return EMPTY

def remove_wins(M,N,K,board):
    #$ Vert Check
    for j in range(M-K+1):
        for i in range(N):
            try:
                if sum([helper(x[i],SEPPO) for x in board[j:K+j]]) == K:
                    idx = random.randint(0,K-1)
                    board[j+idx][i] = EMPTY
            except: pass
            try:
                if sum([helper(x[i],TOZAN) for x in board[j:K+j]]) == K:
                    idx = random.randint(0,K-1)
                    board[j+idx][i] = EMPTY
            except: pass

    #$ Zont Check
    for j in range(M):
        for i in range(N-K+1):
            try:
                if sum([helper(e,SEPPO) for e in board[j][i:i+K]])==K:
                    idx = random.randint(0,K-1)
                    board[j][i+idx] = EMPTY
            except: pass
            try:
                if sum([helper(e,TOZAN) for e in board[j][i:i+K]])==K:
                    idx = random.randint(0,K-1)
                    board[j][i+idx] = EMPTY
            except: pass

    #$ Right Diag Check
    for i in range(M-K+1):
        for j in range(N-K+1):
            try:
                if sum([helper(board[i+l][j+l],SEPPO) for l in range(K)])==K:
                    idx = range(0,K-1)
                    board[i+idx][j+idx] = EMPTY
            except: pass

            try:
                if sum([helper(board[i+l][j+l],TOZAN) for l in range(K)])==K:
                    idx = range(0,K-1)
                    board[i+idx][j+idx] = EMPTY
            except: pass

    #$ Left Diag Check
    for i in range(M-K+1):
        for j in range(N,K-1,-1):
            try:
                if sum([helper(board[i+l][j-l-1],SEPPO) for l in range(K)])==K:
                    idx = range(0,K-1)
                    board[i+idx][j-idx-1] = EMPTY
            except: pass

            try:
                if sum([helper(board[i+l][j-l-1],TOZAN) for l in range(K)])==K:
                    idx = range(0,K-1)
                    board[i+idx][j-idx-1] = EMPTY
            except: pass

    return board

def rand_board(M,N):
    board = [[None] * N]*M
    board = [[rand_help() for e in row] for row in board]
    return board

def argmax(l:list):
    return l.index(min(l)) if abs(min(l)) > max(l) else l.index(max(l))


def stringBoard(board):
    board_str = "\n"
    for row in board:
        buffer = ""
        for e in row:
            board_str += buffer + e
            buffer = " "
        board_str += "\n"
    return board_str

def rand_case(M,N,num):
    board = rand_board(M,N)
    f = [solve(M,N,K,board) for K in range(3,min(M,N)+1)]
    K = argmax(f)+3
    board = remove_wins(M,N,K,board)

    fp = 'TheMonkGame/'
    if num < 10:
        num = "0" + str(num)
    else:
        num = str(num)
    
    with open(fp + 'input/input' + num + '.txt','w') as f:
        f.write(str(M)+" "+str(N)+" "+str(K))
        f.write(stringBoard(board))

    with open(fp + 'output/output' + num + '.txt','w') as f:
        f.write(str(solve(M,N,K,board)))

def test_generator():

    case_num = 0


    num_easy = 5
    num_medium = 10
    num_hard = 5

    #$ Easy
    for _ in range(num_easy):
        rand_case(random.randint(3,6),random.randint(3,6),case_num)
        case_num += 1

    #$ Medium
    for _ in range(num_medium):
        rand_case(random.randint(10,20),random.randint(10,20),case_num)
        case_num += 1
    
    #$ Hard
    for _ in range(num_hard):
        rand_case(random.randint(40,60),random.randint(40,60),case_num)
        case_num += 1


if __name__ == "__main__":
   line = list(map(int,input().split()))
   print(line)