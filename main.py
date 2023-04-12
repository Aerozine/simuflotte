import os
import numpy as np
import flotte as plouf
import genfig as fig
import utils
import scipy.sparse as sc
# path = os.path.abspath(os.getcwd())
# cl = np.loadtxt(path + "/1-cl.txt", dtype=float)
# dom = np.loadtxt(path + "/2-dom.txt", dtype=float)
# num = np.loadtxt(path + "/2-num.txt", dtype=int)
cl, dom, num = utils.loadfile(4, cl=False)
cl = utils.findCL(dom, 2)
contour=np.loadtxt("4-contourObj.txt")
two=np.empty(contour.shape[0])
two.fill(2)
# to fix ?
u= sc.csc_matrix((two, (contour[:,0],contour[:,1])), shape=(cl.shape[0], cl.shape[1])).toarray()
cl=cl+u
#np.savetxt("2-cl.txt", cl)
#=np.load("psi2.npy")
#cl=np.loadtxt("2-cl.txt")
fig.fig1(dom, cl, num)
