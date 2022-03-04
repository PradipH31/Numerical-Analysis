#Pradip Hamal
#Using Bisection Method to solve (x+2)(x+1)^2(x-1)^3(x-2)
import math
a=-1.5
b=2.5

for i in range(20): #start at 0, stop at 20
    #get midpoint
    p = 1/2*(a+b)
    #apply IVT
    fa = (a+2)*((a+1)**2)*a*((a-1)**3)*(a-2)
    fp = (p+2)*((p+1)**2)*p*((p-1)**3)*(p-2)
    if fp==0:
        #zero found
        print("Answer is: ", p)
        break
    elif fa * fp < 0:
        #change upper bound to p
        b = p
    else:
        #change lower bound to p
        a = p