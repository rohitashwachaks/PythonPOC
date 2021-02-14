def DigSum(x):
    i = 0
    while(x//10 > 0):
        s = 0
        while (x > 0):
            s += x%10
            x = x//10
        x = s
        i += 1
    return x, i


q = int(input())
for _ in range(q):
  #  print(_,";")
    n, d = list(map(int,input().split()))
    a, x = DigSum(n)
    b, y = DigSum(d)
    mini = a
    depth = 0
    i = 0
    if(n//10 > 0):
        while(n//10 > 0):
            s = 0
            while (n > 0):
                s += n%10
                n = n//10
            n = s
            i += 1
           # print(s)
            for j in range(10):
                s += b
                #print(s)
                f, t = DigSum(s)
                if f < mini:
                 #   print(f, t)
                    mini = f
                    depth = i+j+1+t
    for j in range(10):
        n += d
        s,t = DigSum(n)
        #print(n, s, t)
        if s < mini:
            mini = s
            depth = x+j+1+t
    print(mini, depth)

