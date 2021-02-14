#!/bin/python3

import sys

def raceAgainstTime(n, mason_height, height, price):
    # Complete this function
    cost=0
    time=0
    final=list()
    delim=max(height)+1
    cur_height=mason_height

    for i in range(n-1):
        
    #  Swap included only if cost reduced    
        while(height[i]>delim):
            temp=final.pop()
            time+=abs(delim-cur_height)
            if(cost+time<0):
                cost+=temp[1]
                time+=temp[2]
            else:
                cost=temp[1]
                time=temp[2]
            cur_height=temp[0]
            delim=temp[3]
    
    #  Mandatory Baton Change if taller
        if(height[i]>cur_height):

            if(len(final)>0)and(price[i]<0):
                here=list()
                here=final[len(final)-1]
                print(height[i],(cost+time+abs(cur_height-height[i])),(abs(here[0]-height[i])))
                if((cost+time+abs(cur_height-height[i]))>(abs(here[0]-height[i]))):
                    cost=price[i]
                    time=abs(here[0]-height[i])
                    cur_height=height[i]
                    print("Updated>>",cur_height,cost,time,delim,"-> ",cost+time)
                    continue

            print("<---->")
            cost+=price[i]
            time+=abs(height[i]-cur_height)
            cur_height=height[i]

            
    #  Change of baton if price is negetive?
        elif(price[i]<0):
            print(final,"(",height[i],abs(cur_height-height[i]),")")
           # print(height[i],"NOW>>",cur_height,cost,time,delim,"-> ",cost+time)
            if(len(final)>0):
                here=list()
                here=final[len(final)-1]
                print(height[i],(cost+time+abs(cur_height-height[i])),(abs(here[0]-height[i])))
                if((cost+time+abs(cur_height-height[i]))>(abs(here[0]-height[i]))):
                    cost=price[i]
                    time=abs(here[0]-height[i])
                    cur_height=height[i]
                    print("Updated>>",cur_height,cost,time,delim,"-> ",cost+time)
                    continue
            
            final.append([cur_height,cost,time,delim])
            delim=cur_height
            cost=price[i]
            time=abs(cur_height-height[i])
            cur_height = height[i]

        print(height[i],"~~",final,cost+time)

    while(len(final)):
        temp=final.pop()
        if(cost+time<0):
            cost+=temp[1]
            time+=temp[2]
        else:
            cost=temp[1]
            time=temp[2]
        cur_height=temp[0]
        delim=temp[3]
        
    return cost+time+n    

n = int(input().strip())
mason_height = int(input().strip())
heights = list(map(int, input().strip().split(' ')))
prices = list(map(int, input().strip().split(' ')))
result = raceAgainstTime(n, mason_height, heights, prices)
print(result)
