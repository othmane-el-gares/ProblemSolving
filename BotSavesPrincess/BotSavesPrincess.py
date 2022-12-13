#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    p=()
    if grid[0][0]=='p':
        p=(1,1)
    elif grid[0][n-1]=='p':
        p=(1,n)
    elif grid[n-1][0]=='p':
        p=(n,1)
    else:
        p=(n,n)
    m=((n+1)//2,(n+1)//2)
    nbv=m[0]-p[0]
    nbh=m[1]-p[1]
    if nbv>0:
        for i in range(nbv):
            print('UP')
    else:
        for i in range(abs(nbv)):
            print('DOWN')
    if nbh>0:
        for i in range(nbh):
            print('LEFT')
    else:
        for i in range(abs(nbh)):
            print('RIGHT')
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)