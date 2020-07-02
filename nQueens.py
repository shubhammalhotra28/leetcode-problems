
def isSafe(row,col,board,n):


    # vertical direction
    i = row-1

    while i>=0:
        if board[i][col]==1:
            return False
        i -= 1

    # uppr left diagonal

    i = row-1
    j = col-1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # upper right diagonal

    i = row - 1
    j = col + 1

    while i >= 0 and j < n:

        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def nQueenHelper(row,n,board):
    #print(row , n)
    if row == n:
        #print("*")
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
        print()
        return

    for col in range(n):
        #print(col)
        if isSafe(row,col,board,n) is True:
            #print("is safe")
            board[row][col] = 1
            nQueenHelper(row+1,n,board)
            board[row][col] = 0

    return


def nQueen(n):
    board = [[0 for j in range(n)] for i in range(n)]

    nQueenHelper(0, n, board)


n = int(input())
nQueen(n)

