import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import dblquad, quad

exact_single = np.pi


def integrand_single(x):
  return x * np.sin(x)


val_single, _ = quad(integrand_single, 0, np.pi)
print(
    f'[Quad] Интеграл: {val_single:.7f}, Погрешность:'
    f' {abs(val_single - exact_single):.2e}'
)

exact_double = 0.5


def integrand_double(y, x):
  return x + y


val_double, _ = dblquad(integrand_double, 0, 1, lambda x: 0, lambda x: x)
print(
    f'[Dblquad] Интеграл: {val_double:.7f}, Погрешность:'
    f' {abs(val_double - exact_double):.2e}'
)

N_values = [10**3, 10**4, 10**5, 10**6]
num_trials = 50 
mean_errors = []

for N in N_values:
  trial_errors = []
  for _ in range(num_trials):
    x_rand = np.random.uniform(0, 1, N)
    y_rand = np.random.uniform(0, 1, N)

    mask = y_rand <= x_rand
    est_integral = np.sum(x_rand[mask] + y_rand[mask]) / N
    trial_errors.append(abs(est_integral - exact_double))

  mean_errors.append(np.mean(trial_errors))

plt.figure(figsize=(8, 5))
plt.loglog(
    N_values,
    mean_errors,
    marker='o',
    color='teal',
    label='Монте-Карло (средняя ошибка)',
)

theoretical_ref = mean_errors[0] * np.sqrt(N_values[0]) / np.sqrt(N_values)
plt.loglog(
    N_values,
    theoretical_ref,
    linestyle='--',
    color='orange',
    label=r'Теория $O(1/\sqrt{N})$',
)

plt.title('Зависимость погрешности метода Монте-Карло от N')
plt.xlabel('N (количество точек)')
plt.ylabel('Средняя абсолютная погрешность')
plt.grid(True, which='both', ls=':')
plt.legend()
plt.show()
