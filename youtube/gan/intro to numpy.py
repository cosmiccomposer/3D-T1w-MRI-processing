import numpy as np 
np
#types of arrays
np.zeros(5)
np.ones(10)
np.full(10,2.5)

#array from a function
a = np.array[1,2,3,5,7,12]
a
#pull a number out of array
a[2] =10 

a 
#creates a range
np.arange(3, 10)

np.linespace(0,100,11)

#modify the number of columns and rows
np.zeros(5,2)

#2d array with a function
n= np.array([1,2,3,
          4,5,6,
          7,8,9])
#call a number from the 2d array 
n= [0,1] =20 #to replace number create this function
n
#rewrite the row 
n[2] = [1,1,1]

#access column with : operator
n[:, 2] =[0,1,2]


#create randomly generated arrays
np.random.seed(2)
np.random.rand(5,2)

#implement a neumerical math function numbers between 0 & 100
np.random.seed(2)
100 * np.random.rand(5,2)

#modify the seed to have specific matrix ranged from low to high 
np.random.seed(2)
np.random.randint(low=0, high=100)

#Element-arrays

a= np.arange(5)
a

#numbers in the array are multiplied by a number
a * 2

#chain multiple maths operations
b = 10 + (a * 2) ** 2 / 100

#combine and compute 2 arrays
#(+ * / -)
a + b/ 10 

#comparison of arrays 
a >=2
#boolean return for which elements in the arrays are true of each other
a[a>b]

#summarize operations
a.max()
a.min()
a.sum()
a.mean()
#standard deviation
a.std()

#multiply vector matricies
def vector_vector_multiplication(u,v):
    assert u.shape[0] = v.shape[0]
    
    n = u.shape[0]
    
    for i in range(n):
        result = result + u[i] * v[i] 
vector_vector_multiplication(u,v)
#derive it's dot product
u.dot(v)
 
 #matrix-vector multiplication
 U = np.array([
     [2,4,5,6,],
     [1,2,1,2] ,
     [3,1,2,1] ,
 ])
 
 def matrix_vector_multiplication(U,v):
     assert U [1] == v.shape[0]
     
     num_rows = U.shape[0]
     result = np.zeros(num_rows)
     
     for i in range(num_rows):
         result[i] = vector_vector_multiplication(U[i], v)
         
    return result


def matrix_matrix_multiplication(U,V):
    assert U.shape[1] == V.shape[0]
    num_rows = U.shape[0]
    num_cols = V.shape[1:]
    
    result = np.zeros((num_rows, num_cols))
    
    for i in range(num_cols):
        vi = V[:, i]
        Uvi = matrix_vector_multiplication(U, vi)
        result[:, i] = Uvi
    
    return result
U.dot(V) 

#Indentity matrices 
I = np.eye(3)
V
V.dot(I)

#inverse
Vs = V[[0,1,2]]
Vs

Vs_inv= np.linalg.inv(Vs)
Vs_inv
Vs_inv.dot(Vs)