def prime_n(n):
    if(n%2)==0:
        return False
    else:
        for i in range(3,n//2,2):
            if(n%i)==0:
                return False
        return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prime=[]
    prime.append(2)
    prime.append(3)
    prime.append(5)
    prime.append(7)
        
    if(n==1):
        print(2)
    elif(n==2):
        print(3)
    elif(n==3):
        print(5)
    elif(n==4):
        print(7)
    else:
        i=2
        mark=2
        while len(prime)<n:
            t1= (6*i)-1
            t2= (6*i)+1
            if(prime_n((6*i)-1)==True):
                prime.append((6*i)-1)
                if len(prime)>=n:
                    mark=i
            if(prime_n((6*i)+1)==True):
                prime.append((6*i)+1)
                if len(prime)>=n:
                    mark=i
            i +=1        
        print(prime[n-1],end=", ")
        print(mark)
