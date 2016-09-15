from numpy import empty
from pylab import plot,show,imshow,gray,savefig,xlabel,ylabel

N = 50    #Number of times to perform iteration
points = 1000 #Pixels along a side (size of matrix to be plotted)



def mandelbrot(N):
    xi=empty([points,points],float)
    for X in range(points):
        x = float((4*X-2*points))/points  #converting pixel coordinate to actual x,y values 
        for Y in range(points):
            y = float((4*Y-2*points))/points
            z0=0.0
            for n in range(N):
                z0 = z0*z0 + complex(x,y)
            
            if abs(z0) < 2:
                xi[X,Y] = abs(z0)
            else:
                xi[X,Y] = 0
    return xi

imshow(mandelbrot(N).T,extent=[-2,2,-2,2])
xlabel("x")
ylabel("y")
savefig("mandelbrotplot.png")
show()
