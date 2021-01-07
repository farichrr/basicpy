y = int(input("input jumlah data: "))
z = 3
matrix = []
print("masukan data")

for i in range(z):
    a = []
    for j in range(y):
        a.append(str(input()))
    matrix.append(a)

    for i in range(z):
        for j in range(y):
            print(matrix[i][j], end = " ")
        print()

