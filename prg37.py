#37.	Python Program to Transpose a Matrix

#Below is a 2x3 matrix and after transpose it will become a 3x2 matrix
X = [[15,8],
    [6 ,7],
    [5 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
