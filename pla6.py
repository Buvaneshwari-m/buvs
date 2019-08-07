    
jo1,jo2=map(str,input().split())
if(len(jo1)!=len(jo2)):
   print("no")
else:
   como1=[jo1.count(a) for a in jo1]
   Timo1=[jo2.count(a) for a in jo2]
if(como1==Timo1):
   print("yes")
else:
   print("no")
