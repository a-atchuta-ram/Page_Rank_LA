##Page Rank vector from dynamical systems point of view

#Example 
## A=[[0,0,1,1/2],[1/3,0,0,0],[1/3,1/2,0,1/2],[1/3,1/2,0,0]]
import numpy as np
def pr(a,n):
    v=[1/n for i in range(0,n)]
    prod=np.dot(a,v)
    print("A.V is =\n")
    print(prod)
    for i in range(1,10):
        prod=np.dot(a,prod) ##
        print("A^{}.V is=".format(i))
        print(prod)
A=[[0,0,1,1/2],[1/3,0,0,0],[1/3,1/2,0,1/2],[1/3,1/2,0,0]]
pr(A,4)
        
    

    