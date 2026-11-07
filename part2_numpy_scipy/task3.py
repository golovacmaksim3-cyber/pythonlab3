import numpy as np

A = np.array([
    [4.0, -1.5, 2.0, 0.5],
    [1.0, 5.0, -2.0, 1.2],
    [-2.0, 1.0, 6.0, -1.0],
    [0.5, 2.0, -1.0, 7.0]
])

B = np.array([11.05, -6.82, 11.5, -0.5])

det_A = np.linalg.det(A)
print(f'det(A) = {det_A}')

if det_A != 0:
  cond_A = np.linalg.cond(A)
  print(f'Число обусловленности: {cond_A}')

  X_inv = np.dot(np.linalg.inv(A), B)

  X_solve = np.linalg.solve(A, B)

  print('Решение (solve):', np.round(X_solve, 1))

  print('Норма разности:', np.linalg.norm(X_inv - X_solve))
  print('Проверка подстановкой (норма невязки):', np.linalg.norm(np.dot(A, X_solve) - B))
else:
  print('Определитель равен нулю, система вырождена.')
