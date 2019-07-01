bb,vad=map(int,input().split())
for j in range(bb+1,vad,1):
    if(n>1):
        for g in range(2,n):
            if(n%g==0):
                break
        else:
            print(n,end=" ")
