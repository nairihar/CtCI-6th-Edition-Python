# TODO :: implement other solution which uses some storage

def newMatrixWithZeros(matrix, row_index, index):
  zero_matrix = []

  for row_i in range(len(matrix)):
    if row_i == row_index:
      zero_matrix.append([0] * len(matrix[row_index]))
      continue
    else:
      zero_matrix.append([])
  
    for i, n in enumerate(matrix[row_index]):
      if i == index:
        zero_matrix[row_i].append(0)
      else:
        zero_matrix[row_i].append(n)

  return zero_matrix

def zeroMatrix(matrix):
  for row_i, row in enumerate(matrix):
    for i, n in enumerate(row):
      if n == 0:
        return newMatrixWithZeros(matrix, row_i, i)


print(zeroMatrix([
  [1, 0],
  [3, 4]
]))

print(zeroMatrix([
  [1, 2, 3],
  [4, 0, 6],
  [7, 8, 9]
]))

