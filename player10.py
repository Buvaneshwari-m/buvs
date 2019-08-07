fi1,fi2=input().split()
count=0
for i in range(0,len(fi1)):
    for j in range(0,i+1):
        if fi1[i]!=fi2[j]:
            count+=1
            break
if count==1:
    print("yes")
else:
    print("no")
