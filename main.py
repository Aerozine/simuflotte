import os
import numpy as np
import flotte as plouf
import  genfig as fig
import utils
path = os.path.abspath(os.getcwd())
cl = np.loadtxt(path + "/1-cl.txt", dtype=float)
dom = np.loadtxt(path + "/1-dom.txt", dtype=int)
num = np.loadtxt(path + "/1-num.txt", dtype=int)
#cl=utils.findCL(dom,2)
#np.save("2-cl.txt",cl)
#cl=np.load("2-cl.txt.npy")
fig.fig1(dom,cl,num)