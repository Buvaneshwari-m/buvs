    
como261=(input())
ti261=0
for i in range(0,len(como261)):
    soo261=(como261[:i]+como261[i+1:])
    if(int(soo261) % 8==0):
        ti261=1
        break
if(ti261==1):
    print("yes")
else:
    print("no")
