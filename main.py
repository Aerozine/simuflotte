import genfig as fig
import utils as ut

for i in range(2, 5):
    fig.figstream(dom, cl, num, i)
    fig.figpressure(dom, cl, num, i)
    print(str(i) + ")\t" + str(fig.getFC(dom, cl, num, i)))


def f(u):
    cl, dom, num = ut.loadfile(4, cl=False)
    cl = ut.findCL(dom, u=u)
    return fig.getFC(dom, cl, num, 4)[1]


a = ut.bissection(f, 1.85, 1.95, 1e-9)
print(a[0])
print(f(a[0]))
