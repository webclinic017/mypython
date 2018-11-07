import numpy as np
import random

def neighborlist(n):
    l=[]
    for x in range(n.shape[0]*n.shape[1]-1):
        if (x+1)%5==0:
            l.append([x,-1,x+5])
        elif x>=((n.shape[0]-1)*n.shape[1]):
            l.append([x,-1,x+1])
        else:
            l.append([x, x+5, x + 1])
    return l

def graphmade(list1):
    graph={}
    for x in list1:
        if x[1]==-1:
            graph.update({x[0]:[x[2]]})
        else:
            graph.update({x[0]:[x[1],x[2]]})
    return graph

#main function#
#generate matrix#
Matrix= np.zeros((5, 5))
for x in range(5):
    for y in range(5):
        Matrix[x][y]=int(random.randrange(0, 10000))
print Matrix

n=[]
for i in range(Matrix.shape[0]*Matrix.shape[1]):
    n.append(i)
tem1=Matrix.shape[0]-1
tem2=Matrix.shape[1]-1
n.append([tem1,tem2])
nlist=neighborlist(Matrix)
graph=graphmade(nlist)
graph.update({24:[0]})
def dfs_paths(graph,root,target,path=None):
    if path is None:
        path=[root]
    if root==target:
        yield path
    for vertex in [x for x in graph[root] if x not in path]:
        for each_path in dfs_paths(graph,vertex,target,path+[vertex]):
            yield each_path
y= list(dfs_paths(graph,13,24))
i=0
j=0
sumall=[]
for x in y:
    sum=0
    for k in x:
        i=int(k/5)
        j=k%5
        sum=sum+Matrix[i][j]
    x.append(sum)
    sumall.append(sum)
np.array(sumall)
x=np,max(sumall)
for i in y:
    if i[-1]==x[1]:
        print i
print y

print graph

