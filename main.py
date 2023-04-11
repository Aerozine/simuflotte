import os
import numpy as np
import flotte as plouf
import  genfig as fig
import utils
path = os.path.abspath(os.getcwd())
#cl = np.loadtxt(path + "/1-cl.txt", dtype=float)
dom = np.loadtxt(path + "/2-dom.txt", dtype=int)
num = np.loadtxt(path + "/2-num.txt", dtype=int)
cl=utils.findCL(dom,2)
fig.fig1(dom,cl,num)