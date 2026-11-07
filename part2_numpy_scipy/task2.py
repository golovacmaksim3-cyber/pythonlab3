import numpy as np


def analyze_route():
  try:
    lengths = np.array(
        [float(x) for x in input('Введите длины через пробел: ').split()]
    )
    speeds = np.array(
        [float(x) for x in input('Введите скорости через пробел: ').split()]
    )
    k, p, t = map(
        float, input('Введите k, p, t через пробел (например, 3 8 1): ').split()
    )
    k, p = int(k), int(p)

    if len(lengths) != len(speeds):
      raise ValueError('Количество длин и скоростей должно совпадать!')
    if not (1 <= k <= p <= len(lengths)):
      raise ValueError('Некорректные индексы участков k и p.')

    path_lengths = lengths[k - 1 : p]
    total_length = np.sum(path_lengths)

    times = lengths / speeds
    total_time = np.sum(times)

    avg_speed = np.sum(lengths) / total_time

    cumulative_times = np.cumsum(times)
    if t > total_time:
      print('Время t превышает общее время в пути.')
      return

    target_idx = np.searchsorted(cumulative_times, t, side='right')
    if target_idx == 0:
      time_from_prev = t
      current_segment = 1
    else:
      time_from_prev = t - cumulative_times[target_idx - 1]
      current_segment = target_idx + 1

    distance_from_start = time_from_prev * speeds[current_segment - 1]

    print(f'S = {total_length} км, T = {round(total_time, 2)} ч, V = {round(avg_speed, 2)} км/ч')
    print(f'Через {t} ч автомобиль на участке {current_segment}, в {round(distance_from_start, 2)} км от его начала')

  except Exception as e:
    print(f'Ошибка ввода/вывода: {e}. Повторите запрос.')


if __name__ == '__main__':
  analyze_route()
