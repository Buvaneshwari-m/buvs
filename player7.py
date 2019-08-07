nimo=list(input())
coro1=len(nimo)
new=''
for v in range (0,coro1,2):
    nimo[v],nimo[v+1]=nimo[v+1],nimo[v]
print(*nimo,sep='')

