from numpy import loadtxt,arange
from pylab import plot,scatter,xlabel,ylabel,show,xlim,ylim


data = loadtxt("millikan.txt",float)
x = data[:,0]
y = data[:,1]

def Ex(N):
    s = 0.0
    for k in range(N):
        s += x[k]
    return float(s/N)

def Ey(N):
    s = 0.0
    for k in range(N):
        s += y[k]
    return float(s/N)

def Exx(N):
    s = 0.0
    for k in range(N):
        s += (x[k])**2
    return float(s/N)

def Exy(N):
    s = 0.0
    for k in range(N):
        s += (x[k])*(y[k])
    return float(s/N)

N = len(x)
m = (Exy(N)-Ex(N)*Ey(N))/(Exx(N)-Ex(N)**2)
c = (Exx(N)*Ey(N)-Ex(N)*Exy(N))/(Exx(N)-Ex(N)**2)

print m
print c

scatter(x,y)
xlabel("Frequency (Hz)")
ylabel("Voltage (V)")
xlim(0,1.5e15)
ylim(0,3.5)

#PART C
x1 = arange(0,1.5e15,.1e15)
y1 = m*x1 + c
plot(x1,y1,"c-")
show()

#Compare best-fit line y=mx+b with the work function
#slope m is equal to h / e where h is Planck's constant and e is electron charge
H = (1.602e-19)*m
print "The calculated value of Planck's constant is ",H
print "The percent error from accepted value is ",100*(H-(6.6207004e-34))/(6.6207004e-34),"%"

