import flotte as plouf
from matplotlib import pyplot as plt
import numpy as np

def fig1(dom,cl,num):
    psi=plouf.laplace(dom,cl,num)
    x,y=np.meshgrid(np.arange(0,psi.shape[1],1),np.arange(0,psi.shape[0],1))
    u,v=plouf.velocity(dom,psi,2)
    plt.streamplot(x,y,u,v,color="#FFFFFF")
    plt.pcolor(psi)
    plt.colorbar()
    plt.show()
