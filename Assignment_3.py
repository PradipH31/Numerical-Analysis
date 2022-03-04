#Pradip Hamal
#MATH 392_01
#Programming Assignment 3: Newton's Method with Horner's Method
#x^4+5x^3-9x^2-85x-136

#Newton's Method
def newt(P):
    maxIt = 1000
    tol = 10**(-5)
    p = 10
    for i in range(maxIt):
        
        #f(p)
        fp,Q1 = horners(P,p)  
        
        #f'(p)
        fprimep,Q2 = horners(Q1,p)  
        
        #Using newton's method to get p_new
        p_new = p - fp/fprimep  
        
        #Checking the p_new for tolerance
        if abs(p - p_new) < tol:
            return p_new
        p = p_new
        
#Horner's method
def horners(P, x0):
    
    #length of the quadratic equation
    n = len(P)
    
    #initialize Q, list of length n-1 with zeroes
    Q = (n - 1) * [0]
    Q[0] = P[0]

    #did an instance of synthetic division
    #start at 1, stop at n - 1
    for i in range(1, n):
        if i == n - 1:
            rem = Q[n - 2] * x0 + P[n - 1]
        else:
            Q[i] = Q[i - 1] * x0 + P[i]
    return rem,Q

# P = x^4 + 5x^3 - 9x^2 - 85x - 136
P = [1, 5, -9, -85, -136]
print(newt(P))




