print ("Enter the number of queens")
N = int(input())
board = [[0]*N for _ in range(N)]  # number of piece and board with row*col ===board[][]
def is_attack(i, j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:  # attack in same row and column
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True # attack in diagonal 
    return False
def queen(n):   # for place in queen
    if n==0:   #queen are placed from that
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not (is_attack(i, j))) and (board[i][j]!=1):  # if not attack or there is value is zero 
                board[i][j] = 1   
                if queen(n-1)==True:
                    return True  #loop goes to starting point 
                board[i][j] = 0   # when n-1 will become 0 s
    return False
queen(N)
for i in board:
    print(i)