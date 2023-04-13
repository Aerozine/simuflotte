import os

import numpy as np

import flotte as plouf

Q = 8


def loadfile(i, cl=True, path=os.path.abspath(os.getcwd())):
    if cl:
        cl = np.loadtxt(path + "/data/" + str(i) + "-cl.txt", dtype=float)
    dom = np.loadtxt(path + "/data/" + str(i) + "-dom.txt", dtype=float)
    num = np.loadtxt(path + "/data/" + str(i) + "-num.txt", dtype=int)
    return cl, dom, num


def findCL(dom):
    cl = np.zeros_like(dom, dtype=float)
    # conditions au limites
    cl[:, -2].fill(Q)
    cl[1, 1:-1] = np.linspace(0, Q, dom.shape[1] - 2)
    cl[-2, 1:-1] = np.linspace(0, Q, dom.shape[1] - 2)
    y, x = firstnumber(dom)
    width = 0
    while dom[y][x + width] != 1:
        width += 1
    xfill = x + int(width / 2)
    for i in range(2, cl.shape[0] - 2):
        for j in range(2, cl.shape[1] - 2):
            if dom[i, j] == 2:
                cl[i, j] = cl[1, xfill]
    return cl


def firstnumber(dom):
    for i in range(2, dom.shape[0] - 2):
        for j in range(2, dom.shape[1] - 2):
            if dom[i][j] != 1:
                return i, j


def getFC(dom, cl, num, number):
    # returns the Force and the circulation
    psi = plouf.laplace(dom, cl, num)
    u, v = plouf.velocity(dom, psi, 2)
    Pp, Px, Py, Pu, Pv = plouf.genpressure(u, v, dom, case4=(number == 4))
    F = plouf.force(Pp, Px, Py)
    # matrix notation to cartesian
    return (F[1], F[0]), plouf.circu(Pv, Pu, Px, Py)
