# Nama  : Firminus Honoratus
# Nim   : 04319001
# Prodi : Teknik Informatika / B



matriks1 = [
    [1, 2, 3],
    [3, 4, 5]
]

matriks2 = [
    [2, 3, 6],
    [4, 1, 5]
]
matriks3 = []

for x in range(0, len(matriks1)):
    row = []
    for y in range(0, len(matriks1[0])):
        total = 0
        for z in range(0, len(matriks1)):
            total = total + (matriks1[x][z] * matriks2[z][y])
        row.append(total)
    matriks3.append(row)
    
for x in range(0, len(matriks3)):
    for y in range(0, len(matriks3[0])):
        print (matriks3[x][y], end=' ')
    print ()