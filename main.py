import os
import numpy as np
import flotte as plouf
import  genfig as fig
import utils
path = os.path.abspath(os.getcwd())
#cl = np.loadtxt(path + "/1-cl.txt", dtype=float)
dom = np.loadtxt(path + "/2-dom.txt", dtype=float)
num = np.loadtxt(path + "/2-num.txt", dtype=int)
cl=utils.findCL(dom,2)
#np.savetxt("2-cl.txt",cl)
#a=np.load("psi2.npy")
#cl=np.load("2-cl.txt.npy")
fig.fig1(dom,cl,num)