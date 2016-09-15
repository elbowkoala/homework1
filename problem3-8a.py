from numpy import loadtxt
from pylab import scatter,xlabel,ylabel,show


data = loadtxt("millikan.txt",float)
x = data[:,0]
y = data[:,0]

scatter(x,y)
xlabel("x")
ylabel("y")
show()
