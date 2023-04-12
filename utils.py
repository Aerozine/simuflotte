import numpy as np
import os
Q=8
def loadfile(i,cl=True,path = os.path.abspath(os.getcwd())):
    if cl:
        cl = np.loadtxt(path + "/"+str(i)+"-cl.txt", dtype=float)
    dom = np.loadtxt(path + "/"+str(i)+"-dom.txt", dtype=float)
    num = np.loadtxt(path + "/"+str(i)+"-num.txt", dtype=int)
    return cl , dom , num
def findCL(dom,h):
    cl=np.zeros_like(dom,dtype=float)
    #conditions au limites
    cl[:,-2].fill(Q)
    cl[1,1:-1]=np.linspace(0,Q,dom.shape[1]-2)
    cl[-2,1:-1]=np.linspace(0,Q,dom.shape[1]-2)
    y,x=firstnumber(dom,cl)
    width=0
    a=cl[y][x]
    while(dom[y][x+width]!=1):
        width+=1
    xfill=cl.shape[1]-x-int(width/2)-1
    for i in range(2,cl.shape[0]-2):
        for j in range(2, cl.shape[1] - 2):
            if(dom[i,j]==2):
                cl[i,j]=cl[-2,xfill]
    return cl
def firstnumber(dom,cl):
    for i in range(2,cl.shape[0]-2):
        for j in range(2, cl.shape[1] - 2):
            if(dom[i][j]!=1):
                return (i,j)