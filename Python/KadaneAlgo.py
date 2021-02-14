t = int(input().strip())
for a0 in range(t):
    n,k = [int(i) for i in input().strip().split()]
    a = [int(r) for r in input().strip().split()]
    a=a+a
    neg=0
    s=0
    
    while(a[0]<0):
        z=a.pop(0)
        neg+=z
            
    max_so_far = 0 
    max_ending_here = 0
      
    for i in range(0, len(a)):
        max_ending_here += a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
            s=1

    #max_ending_here+=neg
    if(int((max_ending_here*(k/2))+neg)>(max_so_far) and s==0):
        print(int(k*max_ending_here/2))
    else:
        print(max_so_far)
