import flotte as plouf
from matplotlib import pyplot as plt
import numpy as np

def fig1(dom,cl,num):
    psi=plouf.laplace(dom,cl,num)
    plt.contourf(psi)
    print(psi)
    plt.show()
