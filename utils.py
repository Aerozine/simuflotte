import os

import numpy as np

Q = 8


def loadfile(i, cl=True, path=os.path.abspath(os.getcwd())):
    if cl:
        cl = np.loadtxt(path + "/data/" + str(i) + "-cl.txt", dtype=np.float64)
    dom = np.loadtxt(path + "/data/" + str(i) + "-dom.txt", dtype=np.float64)
    num = np.loadtxt(path + "/data/" + str(i) + "-num.txt", dtype=int)
    return cl, dom, num


def findCL(dom, u=None):
    cl = np.zeros_like(dom, dtype=np.float64)
    # conditions au limites
    cl[1:-1, -2].fill(Q)
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
                if u is not None:
                    cl[i, j] = u
                else:
                    cl[i, j] = cl[1, xfill]
    return cl


def firstnumber(dom):
    for i in range(2, dom.shape[0] - 2):
        for j in range(2, dom.shape[1] - 2):
            if dom[i][j] != 1:
                return i, j


def getInterestPoint(u, v, dom, case4=False, contourpath="data/4-contourObj.txt"):
    # compute the circulation over the body
    if not case4:
        x, y = firstnumber(dom)
        xdiff = 0
        ydiff = 0
        while dom[x + xdiff, y] == 2:
            xdiff += 1
        while dom[x, y + ydiff] == 2:
            ydiff += 1
        x -= 1
        y -= 1
        # obscure method to trace a rectangle
        xdiff += 1
        ydiff += 1
        a = np.arange(x, x + xdiff)
        e = np.full_like(a, y)
        f = np.arange(y, y + ydiff)
        b = np.full_like(f, x + xdiff)
        c = np.arange(x + xdiff, x, -1)
        g = np.full_like(c, y + ydiff)
        h = np.arange(y + ydiff, y, -1)
        d = np.full_like(h, x)
        tabx = np.concatenate((a, b, c, d, x), axis=None)
        taby = np.concatenate((e, f, g, h, y), axis=None)
    else:
        contour = np.loadtxt(contourpath)
        tabx = contour[:, 0]
        taby = contour[:, 1]
    U = np.empty_like(tabx, dtype=np.float64)
    V = np.empty_like(tabx, dtype=np.float64)
    for i in range(tabx.shape[0]):
        U[i] = u[int(tabx[i]), int(taby[i])]
        V[i] = v[int(tabx[i]), int(taby[i])]
    return tabx, taby, U, V


def bissection(f, x0, x1, tol):
    x = 0
    statut = 0
    tab = [x, statut]
    x_0 = x0
    x_1 = x1
    f_x0 = f(x0)
    f_x1 = f(x1)
    while abs(f_x0 - f_x1) > tol:
        x2 = (x_0 + x_1) / 2
        f_x2 = f(x2)
        if f_x0 * f_x2 < 0:
            x_0 = x_0
            x_1 = x2
            f_x1 = f_x2
        elif f_x1 * f_x2 < 0:
            x_1 = x_1
            x_0 = x2
            f_x0 = f_x2
        else:
            print("Valeur trouvée sans approximation")
            tab = [x2, 0]
            return tab
    tab = [x2, 0]
    return tab
