import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-8, 8, 2000)
y = 4 / (x**2 - 4)

y[np.abs(x - 2) < 0.05] = np.nan
y[np.abs(x + 2) < 0.05] = np.nan

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='purple', label='y(x) = 4 / (x^2 - 4)')

plt.axvline(x=2, color='gray', linestyle='--', label='Асимптота x = 2')
plt.axvline(x=-2, color='gray', linestyle='--', label='Асимптота x = -2')

plt.ylim(-10, 10)
plt.xlim(-8, 8)

plt.title('График функции с разрывами')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.show()
