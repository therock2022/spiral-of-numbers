n = int(input()) #размер матрицы
matrix = [[0] * n for i in range(n)] #создание матрицы нужного размера, заполнена 0
count = 0 #количество заполненых ячеек
for i in range(n):  # заполнение первой строки
    count += 1
    matrix[0][i] = count
j = 0 # последняя заполненая ячейка
i = n-1
n -= 1  # устанавливаем размер 1 блока 1 витка
while len(matrix)**2 != count:  # условие выхода из цикла
    for k in range(n):  # движение вниз
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








