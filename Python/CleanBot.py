import math

def nextMove(n,posr,posc,r,c,grid):
    h=c-posc
    v=r-posr
    if(h==0 and v==0):
            print("CLEAN")
            return 1
    else:
        if h<0:
            print("LEFT")
            h+=1
        elif h>0:
            print("RIGHT")
            h-=1
        elif v<0:
            print("UP")
            v+=1
        elif v>0:
            print("DOWN")
            v-=1        
        
    return 1

def next_move(posr, posc, board):
    val='d'
    dirt=[]
    keys=0
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j])==val:
                dirt.append([keys,i,j])
                keys+=1
    dist=[]
    for key in dirt:
        b2d=abs(math.sqrt(((key[1]-posr)**2)+((key[2]-posc)**2)))
        dist.append([key[0],b2d])
            
    minm = 0.0
    dest_key=0
#ASSING MINM AN APPROPRIATE VALUE
    for key in dist:
        minm=key[1]
        dest_key=key[0]
        break
    for key in dist:
        if(key[1]<minm):
            minm=key[1]
            dest_key=key[0]
                
    for key in dirt:
        if(dest_key==key[0]):
            nextMove(5,posr,posc,key[1],key[2],board)
            board[key[1]][key[2]]='-'
            board[posr][posc]='-'
            posr=key[1]
            posc=key[2]
            if(board[posr][posc])!='d':
                board[posr][posc]='b'           
               
    keys-=1

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
