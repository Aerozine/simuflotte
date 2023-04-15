import genfig as fig
import utils as ut

for i in range(2, 5):
    cl, dom, num = ut.loadfile(i, cl=False)
    cl = ut.findCL(dom)
    fig.figstream(dom, cl, num, i)
    fig.figpressure(dom, cl, num, i)
    print(str(i) + ")\t" + str(fig.getFC(dom, cl, num, i)))
# plot de la circu vide en stream5.png
cl, dom, num = ut.loadfile(4, cl=False)
cl = ut.findCL(dom, u=1.8978822708129879)
fig.figstream(dom, cl, num, 5)


def f(u):
    cl, dom, num = ut.loadfile(4, cl=False)
    cl = ut.findCL(dom, u=u)
    return fig.getFC(dom, cl, num, 4)[1]


# calcul pour trouver la circulation nulle
a = ut.bissection(f, 1.85, 1.95, 1e-9)
print(a[0])
print(f(a[0]))
