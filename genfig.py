import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import flotte as plouf


def fig1(dom, cl, num):
    psi = plouf.laplace(dom, cl, num)
    #np.savetxt("psi.txt",psi)
    #psi=np.loadtxt("psi.txt")
    u, v = plouf.velocity(dom, psi, 2)

    y, x = np.meshgrid(np.arange(0, u.shape[0], 1), np.arange(0, u.shape[1], 1))

    Pp,Px,Py,Pu,Pv=plouf.genpressure(u,v,dom,case4=False)
    plt.pcolor(plouf.pressure(u.T,v.T), cmap='turbo')
    print(plouf.force(Pp,Px,Py))
    print(plouf.circu(Pu,Pv,Px,Py))
    print(plouf.circu(Pv,Pu,Px,Py))
    u=u.T
    v=v.T
    #plt.colorbar()

    #plt.streamplot(y,x, v, u, color="#000000", arrowstyle='-', minlength=0.3, broken_streamlines=False,arrowsize=0.1)
    #plt.pcolor(psi.T, cmap='turbo')
    #plt.colorbar()

    plt.show()



