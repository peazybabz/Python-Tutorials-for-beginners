#38.	Python Program to Multiply Two Matrices

# 3x3 matrix
X = [[1,8,3],
    [4 ,4,6],
    [3 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [1,6,3,0],
    [4,1,4,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
