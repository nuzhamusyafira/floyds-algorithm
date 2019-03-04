def floyd(m2,n2):
	d=[]
	p=[]
	inf=1000
	for x in m2:
		temp=[]
		temp2=[]
		for y in x:
			temp.append(y)
			temp2.append(-1)
		d.append(temp)
		p.append(temp2)
	for x in range(n2):
		for y in range(n2):
			if x==y:
				p[x][y]=0
			elif d[x][y]!=inf:
				p[x][y]=x
			else:
				p[x][y]=-1
	for x in range(n2):
		for y in range(n2):
			for z in range(n2):
				if d[y][x]+d[x][z]<d[y][z]:
					d[y][z]=d[y][x]+d[x][z]
					p[y][z]=p[x][z]
	return d,p

def printAll(p2,n2):
	print("")
	for x in range(n2):
		for y in range(n2):
			if x!=y and p2[x][y]!=-1:
				print("Path dari",x+1,"ke",y+1,"=",x+1,"->",end='')
				printPath(p2,x,y)
				print("",y+1)

def printPath(p3,x2,y2):
	if p3[x2][y2]!=x2:
		printPath(p3,x2,p3[x2][y2])
		print("",p3[x2][y2]+1,"->",end='')

inf=1000
m=[
   [0,1,5,7,9,inf],
   [1,0,6,7,3,inf],
   [5,6,0,9,inf,8],
   [7,7,9,0,8,3],
   [9,3,inf,8,0,inf],
   [inf,inf,8,3,inf,0]
  ]
n=len(m)
print("\nTabel jarak mula-mula:")
for x in m:
	print(x)
result,path=floyd(m,n)
print("\nTabel jarak terpendek:")
for x in result:
	print(x)
printAll(path,n)