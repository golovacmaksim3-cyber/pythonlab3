import numpy as np

expenses = np.array([3200, 3100, 2600, 1900, 1500, 1300, 1250, 1400, 1800, 2300, 2900, 3500])

winter_sum = expenses[11] + expenses[0] + expenses[1]
summer_sum = np.sum(expenses[5:8])

print(f'Зима: {winter_sum}, лето: {summer_sum} -> больше тратится зимой')

max_val = np.max(expenses)
max_months = np.where(expenses == max_val)[0] + 1 

print(f'Максимум ({max_val}) в месяцах: {max_months.tolist()}')
