import numpy as np
from matplotlib import pyplot as plt

import flotte as plouf


def figstream(dom, cl, num, number, show=False):
    plt.figure()
    psi = plouf.laplace(dom, cl, num)
    u, v = plouf.velocity(dom, psi, 2)
    y, x = np.meshgrid(np.arange(0, u.shape[0], 1), np.arange(0, u.shape[1], 1))
    plt.streamplot(y, x, v.T, u.T, color="#000000", arrowstyle='-', minlength=0.3, broken_streamlines=False,
                   arrowsize=0.1)
    plt.pcolor(psi.T, cmap='turbo')
    plt.colorbar()
    plt.xlabel('Axe x')
    plt.ylabel('Axe y')
    plt.savefig("pictures/stream" + str(number) + ".png")
    if show:
        plt.show(block=False)
    plt.close()


def figpressure(dom, cl, num, number, show=False):
    plt.figure()
    psi = plouf.laplace(dom, cl, num)
    u, v = plouf.velocity(dom, psi, 2)
    plt.pcolor(plouf.pressure(u.T, v.T), cmap='turbo')
    plt.colorbar()
    plt.savefig("pictures/pressure" + str(number) + ".png")
    if show:
        plt.show(block=False)
    plt.close()


def getFC(dom, cl, num, number):
    # returns the Force and the circulation
    psi = plouf.laplace(dom, cl, num)
    u, v = plouf.velocity(dom, psi, 2)
    Ix, Iy, Iu, Iv = plouf.getIntrestPoint(u, v, dom, case4=(number == 4))
    Ip = plouf.pressure(Iu, Iv)
    F = plouf.force(Ip, Ix, Iy)
    return F, plouf.circu(Iu, Iv, Iy, Ix)
