kio26,tig26=map(int,input().split())
oo26=[]
for _ in range(kio26):
	oo26.append(sorted(list(map(int,input().split()))))
for i in range(kio26-1):
	for j in range(tig26):
		for k in range(kio26-i):
			if(oo26[i][j]>oo26[i+k][j]):
				oo26[i][j],oo26[i+k][j]=oo26[i+k][j],oo26[i][j]
for i in oo26:
	print(*i,sep=' ')     
