n = int(input()) # matrix size
matrix = [[0] * n for i in range(n)] #build matrix, exist 0
count = 0 #number of full cells
for i in range(n):  # filling first string
    count += 1
    matrix[0][i] = count
j = 0 # last filled string
i = n-1
n -= 1  # set size 1 block 1 cicle
while len(matrix)**2 != count:  # условие выхода из цикла
    for k in range(n):  # movemend downward
        j += 1
        count += 1
        matrix[j][i] = count  # заполнение матрицы
    for k in range(n):  # движение влево
        i -= 1
        count += 1
        matrix[j][i] = count
    for k in range(n-1):  # движение вверх
        j -= 1
        count += 1
        matrix[j][i] = count
    for k in range(n-1):  # движение вправо
        i += 1
        count += 1
        matrix[j][i] = count
    n -= 2  # обеспечиваем переход на внутренний виток
for i in range(len(matrix)):  # вывод полученной матрицы
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()








