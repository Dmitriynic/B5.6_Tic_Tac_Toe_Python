#номер вводимой клетки 0-2

k = 0
a = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
dict1 = {'x' : 0, 'o': 0}
dict2 = {'x' : 0, 'o': 0}
dict3 = {'x' : 0, 'o': 0}
dict4 = {'x' : 0, 'o': 0}
dict5 = {'x' : 0, 'o': 0}
dict6 = {'x' : 0, 'o': 0}
dict7 = {'x' : 0, 'o': 0}
dict8 = {'x' : 0, 'o': 0}
col = (dict1, dict2, dict3)
row = (dict4, dict5, dict6)
diag = (dict7, dict8)

for i in range(9) :
    var = input("Введите x или o:")
    x = int(input("Введите номер клетки по горизонтали:"))
    y = int(input("Введите номер клетки по вертикали:"))
    a[y][x] = '%s' % var
    print('\n')
    for l in a:
        print('\t'.join(map(str, l)))
    print("\n")
    col[y][var] += 1
    row[x][var] += 1
    if x == y and x != 1 and y != 1:
        diag[0][var] += 1
    else:
        if x == y:
            diag[0][var] += 1
            diag[1][var] += 1
        else:
            if (x + y) % 2 == 0:
                diag[1][var] += 1
    for j in range(3):
        if col[j][var] == 3 or row[j][var] == 3:
            k = 1
    if diag[0][var] == 3 or diag[1][var] == 3:
        k = 1
    if k == 1:
         print("Победили " + var)
         break


