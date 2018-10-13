def rotateMatrix(matrix):
  rotated_mattrix = []

  for j in range(len(matrix)):
    rotated_mattrix.append([None] * len(matrix))

  for row_i, row in enumerate(matrix):
    for i, n in enumerate(row):
      rotated_mattrix[i][len(row) - 1 - row_i] = n
  
  return rotated_mattrix

print(rotateMatrix([
  [1, 2],
  [3, 4]
]))

print(rotateMatrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))
