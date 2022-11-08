n = int(input()) # matrix size
matrix = [[0] * n for i in range(n)] #build matrix, exist 0
count = 0 #number of full cells
for i in range(n):  # filling first string
    count += 1
    matrix[0][i] = count
j = 0 # last filled string
i = n-1
n -= 1  # set size 1 block 1 cicle
while len(matrix)**2 != count:  # condition ofquit cicle
    for k in range(n):  # movement downward
        j += 1
        count += 1
        matrix[j][i] = count  # filling matrix
    for k in range(n):  # movement left
        i -= 1
        count += 1
        matrix[j][i] = count
    for k in range(n-1):  # movement upward
        j -= 1
        count += 1
        matrix[j][i] = count
    for k in range(n-1):  # movement right
        i += 1
        count += 1
        matrix[j][i] = count
    n -= 2  
for i in range(len(matrix)):  # output of full matrix
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()








