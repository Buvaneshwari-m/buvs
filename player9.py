query,sql=map(int,input().split())
count=0
for meow in range(query,sql+1):
    if meow>1:
        for n in range(2,m):
            if(meow%n==0):
                break
        else:
            count=count+1
print(count)
