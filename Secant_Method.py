#Pradip Hamal
#MATH 392_01
#Programming Assignment 2
#Solving the functionX using secant method with p0 and p1

#import for cos and e
import math

#secant as a function to get the solution
def secant(p0,p1):
    maxIt = 1000
    
    #accuracy 10^-5
    tol = 10**(-5)
    for i in range(maxIt):  
        
        #divided the secant method to numerator and denominator
        numerator = functionX(p1)*(p1-p0)
        denominator = functionX(p1)-functionX(p0)
        p_new = p1 - numerator/denominator
        
        #check if successive use of secant method produces solution
        #within required accuracy
        if abs(p1 - p_new) < tol:

            #if it does, return the value
            return p1
        
        #change the p0 and p1
        p0 = p1
        p1 = p_new

#created a function for the equation to be solved
def functionX(x):
    return (math.e**x+2**-x+2*math.cos(x)-6)

p0 = 1
p1 = 2
p = secant(p0,p1)
print(p)


