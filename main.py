import genfig as fig
import utils

for i in range(2, 5):
    cl, dom, num = utils.loadfile(i, cl=False)
    cl = utils.findCL(dom)
    fig.figstream(dom, cl, num, i)
    fig.figpressure(dom, cl, num, i)
    print(str(i) + ")\t" + str(fig.getFC(dom, cl, num, i)))
