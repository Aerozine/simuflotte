import numpy as np

Q=8

def findCL(dom,h):
    cl=np.zeros_like(dom)
    #conditions au limites
    cl[:][0].fill(Q)
    cl[0][:]=np.arange(0,dom.shape[1]+h,h)
    cl[-1][:]=np.arange(0,dom.shape[1]+h,h)
    tmp=cl[2:-2][2:-2]
    x,y=firstnumber(cl)
    width=0
    while(cl[x][y+width]!=0):
        width+=1
    qfill=(cl.shape[1]-y-int(width/2)+1)*h
    for i in range(2,cl.shape[0]-2):
        for j in range(2, cl.shape[1] - 2):
            if(dom[i][j]!=1):
                cl[i][j]
def firstnumber(cl):
    for x in range(2,cl.shape[0]-2):
        for y in range(2, cl.shape[1] - 2):
            if(cl[x][y]!=0):
                return x,y
