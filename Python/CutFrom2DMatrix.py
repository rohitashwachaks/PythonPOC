#!/bin/python3

import sys


def kadane(a,size): 
    max_so_far = -5001
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0,size):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    return max_so_far,start,end

def max_submatrix(A,n,m):
    l=0
    r=0
    cur_sum=0
    max_sum=(-5000*m)-1
    max_left=0
    max_right=0
    max_up=0
    max_down=0
    for l in range(0,n):
        buffer=list()
        left=0
        right=0
        buffer=A[l]
        cur_sum,left,right=kadane(buffer,m)
        if(cur_sum>max_sum):
            max_left=left
            max_right=right
            max_up=l
            max_down=l
            max_sum=cur_sum
        
        for r in range(l+1,n):
            buffer = [sum(i) for i in zip(buffer,A[r])]
#            print(buffer)
            cur_sum,left,right=kadane(buffer,m)    
            if(cur_sum>max_sum):
                max_left=left
                max_right=right
                max_down=r
                max_sum=cur_sum
    return max_left,max_right,max_up,max_down,max_sum

def check(A,n,m,k,min_left,min_right,min_up,min_down,min_sum):
#    l=0
 #   r=0
    cur_sum=0
    if(k==1):
        for l in range(n):
            for r in range(m):
                if(cur_sum>min_sum):
                    min_left=l
                    min_right=r
                    min_up=l
                    min_down=l
                    min_sum=cur_sum
        min_sum*=-1
    for l in range(0,n):
        for r in range(0,m-k+1):
            buffer=list()
            buffer=A[l][r:r+k]
            buffer = [i*-1 for i in buffer]
#            print(buffer)
            cur_sum,left,right=kadane(buffer,k)
            if(cur_sum>min_sum):
                min_left=r
                min_right=r+k-1
                min_up=l
                min_down=l
                min_sum=cur_sum
    min_sum*=-1
    return(min_left,min_right,min_up,min_down,min_sum)


def min_subarray(A,n,m,k):
    
    min_sum_a=-(5000*k)-1
    min_left_a=0
    min_right_a=0
    min_up_a=0
    min_down_a=0
    min_left_a,min_right_a,min_up_a,min_down_a,min_sum_a= check(A,n,m,k,min_left_a,min_right_a,min_up_a,min_down_a,min_sum_a)
#    print(min_left_a,min_right_a,min_up_a,min_down_a,min_sum_a)
    
    B=list()
    for row in A :
        B = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    
    min_sum_b=-(5000*k)-1
    min_left_b=0
    min_right_b=0
    min_up_b=0
    min_down_b=0
    min_up_b,min_down_b,min_left_b,min_right_b,min_sum_b= check(B,m,n,k,min_left_b,min_right_b,min_up_b,min_down_b,min_sum_b)
#    print(min_left_b,min_right_b,min_up_b,min_down_b,min_sum_b)
    if(min_sum_b<min_sum_a):
        return min_left_b,min_right_b,min_up_b,min_down_b,min_sum_b
    return min_left_a,min_right_a,min_up_a,min_down_a,min_sum_a
    
        
            

def cutAStrip(A,n,m,k):
    # Complete this function
    max_sum=0
    max_left=0
    max_right=0
    max_up=0
    max_down=0
    max_left,max_right,max_up,max_down,max_sum = max_submatrix (A,n,m)
    # Thus index is A[max_up][max_left]->A[max_down][max_right]
#    print(max_left,max_right,max_up,max_down)
    
    min_left=0
    min_right=0
    min_up=0
    min_down=0
    min_left,min_right,min_up,min_down,min_sum = min_subarray (A,n,m,k)
    if(min_left==min_right):#VERTICAL
        for i in range(min_up,min_down+1):
            A[i][min_left]=0
    elif (min_up==min_down):#HORIZONTAL
        for i in range(min_left,min_right+1):
            A[min_up][i]=0
    max_left,max_right,max_up,max_down,max_sum = max_submatrix (A,n,m)   
#    print(min_left,min_right,min_up,min_down,min_sum)
    # Thus index is A[min_up][min_left]->A[min_down][min_right]
'''    
    #Check For Overlap:
    if((min_left<=max_right)and(min_right>=max_left)and(min_up<=max_down)and(min_down>=max_up)):
        if(min_left==min_right):#VERTICAL
            
        elif (min_up==min_down):#HORIZONTAL
            
    else:
'''        
    return(max_sum)

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    A = []
    for A_i in range(n):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = cutAStrip(A,n,m,k)
    print(result)
