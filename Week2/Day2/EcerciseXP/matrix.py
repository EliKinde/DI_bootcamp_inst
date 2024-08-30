matrix ='''7ii
Tsx
h%?
i #
sM
$a
#t%
^r!'''
#print(matrix)
matrix_list = matrix.split('\n')
matrix_list[4] += " "
matrix_list[5] += " "
#print(matrix_list)
column_01 = [row[0] for row in matrix_list]
column_02 = [row[1] for row in matrix_list]
column_03 = [row[2] for row in matrix_list]

new_matrix = column_01 + column_02 + column_03
#print(new_matrix)
i = 0
got = []
for char in new_matrix:
    for row in char:
        if row.isalpha():
            got.append(row)
    got.append(" ")
print(got)
for row in char:
    if row == " ":
        Matrix_soltion =
print("".join(Matrix_soltion))
print(len(Matrix_soltion))
