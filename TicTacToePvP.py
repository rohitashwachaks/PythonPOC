#!/usr/bin/env python
# coding: utf-8

#Python Script for TicTacToe game (Player vs Player)

class style:
    MAGENTA = '\033[96m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def initBoard():
    board = []
    for i in range(0,size,1):
        board.append(['-','-','-'])
    return board

def checkWinStatus():
    winCondition = (['O','O','O'],['X','X','X'])
    flag = -1
    
    for x in winCondition:
        #Row Check
        for row in board:
            if row == x:
                flag = winCondition.index(x)
                
        #Col Check
        for j in range(0,size,1):
            temp = []
            for i in range(0,size,1):
                temp.append(board[i][j])
            if temp == x:
                flag = winCondition.index(x)
                
        #Diagonal Check
        diag_principal = []
        diag_second = []
        for i in range(0,size,1):
            diag_principal.append(board[i][i])
            diag_second.append(board[2-i][i])
            if diag_principal == x or diag_second == x:
                flag = winCondition.index(x)
        
    return flag

def checkValidInput(r,c):
    try:
        if(r>=0 and r<size and c>=0 and c<size):
            if(board[r][c] == '-'):
                return True
            else:
                return False
        else:
            return False
    except:
        return False



def drawBoard(turn, winPlayer):
    print("Play Number:",turn)
    
    print("\n col:",end='     ')
    for i in range(0,size,1):
        print(i,end='    ')
    for i in range(0,size,1):
        print("\n row:",i,board[i])
    
    if(turn !=0):
        if(winPlayer != -1):
            print(style.BOLD+style.RED+"\nWinner: Player"+style.END,winPlayer)
        else:
            print("\nCurrent Player: ",turn%2)



def fillBoard(r,c,curPlayer):
    board[r][c] = marker[curPlayer]
    winner = checkWinStatus()
    return winner

def takeInput():
    count = 0
    for i in range(0,size,1):
        for j in range(0,size,1):
            if board[i][j] == '-':
                count +=1
    if count ==0:
        return -500,-500
        
    try:
        ip = input("Enter Co-ordinates (r, c): ")
        if (ip == "esc"):
            return -100,-100
        r,c = map(int,ip.split(','))
        if checkValidInput(r,c):
            return r,c
        else:
            return -1,-1
    except:
        return -1,-1




def nextPlay(r,c,playNumber):
    curPlayer  =playNumber%2
    winner = fillBoard(r,c,curPlayer)
    board[r][c] = marker[curPlayer]
    return winner,playNumber+1

def Play():
    winPlayer = -1
    playNumber = 0
    
    while(winPlayer== -1):
        print(style.BOLD+"\nPlayer "+str(playNumber%2)+style.END)
        print(style.BOLD+"\nMarker '"+marker[playNumber%2]+"'"+style.END)
        ip_r,ip_c = takeInput();
        
        if (ip_r == -100 and ip_c == -100):
            print(style.BOLD+"Game Interrupted. Terminating"+style.END)
            break
        
        elif (ip_r == -1 and ip_c == -1):
            print("Invalid Input")
            continue
        
        elif (ip_r == -500 and ip_c == -500):
            print("This Match is a Draw")
            break
        
        else:
            winPlayer,playNumber = map(int,nextPlay(ip_r,ip_c,playNumber))
            drawBoard(playNumber,winPlayer)

size = 3
marker = ('O','X')
board = initBoard()
drawBoard(0,0)
Play()
print(style.BOLD+"\nGame Over"+style.END)
