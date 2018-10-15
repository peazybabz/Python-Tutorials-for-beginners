#36.	Python Program to Add Two Matrices

#We will use nested loop

X = [[17,7,3],
    [9 ,5,6],
    [1 ,8,9]]

Y = [[5,7,2],
    [6,8,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)