import numpy as np

Q=8

def findCL(dom,h):
    cl=np.zeros_like(dom,dtype=float)
    #conditions au limites
    cl[0,:].fill(Q)
    cl[:,0]=np.linspace(8,0,dom.shape[0])
    cl[:,-1]=np.linspace(8,0,dom.shape[0])
    tmp=cl[2:-2][2:-2]
    x,y=firstnumber(dom,cl)
    width=0
    while(cl[x][y+width]!=0):
        width+=1
    yfill=cl.shape[1]-y-int(width/2)+1
    for i in range(2,cl.shape[0]-2):
        for j in range(2, cl.shape[1] - 2):
            if(dom[i,j]!=1):
                cl[i,j]=cl[yfill,0]
    return cl
def firstnumber(dom,cl):
    for x in range(2,cl.shape[0]-2):
        for y in range(2, cl.shape[1] - 2):
            if(dom[x][y]!=1):
                return (x,y)