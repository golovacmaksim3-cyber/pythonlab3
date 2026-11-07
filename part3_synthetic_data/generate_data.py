import argparse
import sys
import numpy as np
import pandas as pd


class InvalidConfigError(Exception):
  """Кастомное исключение для некорректных параметров командной строки."""

  pass


def generate_sales_data(seed, years, stores_count):
  """Генерирует датасет по продажам с заданными закономерностями."""
  np.random.seed(seed)

  start_date = pd.Timestamp('2023-01-01')
  days_count = years * 365
  dates = pd.date_range(start=start_date, periods=days_count, freq='D')

  stores = [f'Store_{i+1}' for i in range(stores_count)]
  cities = ['Minsk', 'Grodno', 'Brest', 'Vitebsk', 'Gomel'][:stores_count]
  store_city_map = dict(zip(stores, cities))

  categories = ['Electronics', 'Clothing', 'Home']
  products = {
      'Electronics': ['Phone', 'Laptop', 'Tablet'],
      'Clothing': ['Jacket', 'Jeans', 'T-Shirt'],
      'Home': ['Lamp', 'Chair'],
  }

  all_rows = []

  for date in dates:
    daily_transactions = np.random.randint(50, 100)
    for _ in range(daily_transactions):
      store_id = np.random.choice(stores)
      city = store_city_map[store_id]

      category = np.random.choice(categories)
      product = np.random.choice(products[category])

      is_weekend = 1 if date.dayofweek >= 5 else 0
      season_factor = 1.2 if is_weekend else 1.0

      base_qty = np.random.poisson(lam=3) + 1
      qty = int(base_qty * season_factor)

      base_prices = {
          'Phone': 500,
          'Laptop': 1000,
          'Tablet': 300,
          'Jacket': 100,
          'Jeans': 50,
          'T-Shirt': 20,
          'Lamp': 40,
          'Chair': 80,
      }
      price = base_prices[product] * np.random.normal(1.0, 0.05)
      cost = price * 0.7

      promo = 1 if np.random.rand() < 0.2 else 0
      if promo:
        price *= 0.85
        qty = int(qty * 1.5)

      payment_method = np.random.choice(
          ['cash', 'card', 'online'], p=[0.4, 0.45, 0.15]
      )

      all_rows.append({
          'date': date,
          'store_id': store_id,
          'city': city,
          'category': category,
          'product': product,
          'qty': qty,
          'price': round(price, 2),
          'cost': round(cost, 2),
          'promo': promo,
          'payment_method': payment_method,
      })

  df = pd.DataFrame(all_rows)

  anomaly_idx = np.random.choice(
      df.index, size=int(0.01 * len(df)), replace=False
  )
  df.loc[anomaly_idx, 'qty'] *= 10

  na_price_idx = np.random.choice(
      df.index, size=int(0.005 * len(df)), replace=False
  )
  df.loc[na_price_idx, 'price'] = np.nan

  na_pay_idx = np.random.choice(
      df.index, size=int(0.005 * len(df)), replace=False
  )
  df.loc[na_pay_idx, 'payment_method'] = np.nan

  return df


def main():
  parser = argparse.ArgumentParser(
      description='Генератор синтетических данных о продажах.'
  )
  parser.add_argument('--seed', type=int, default=42, help='Seed для генератора')
  parser.add_argument(
      '--years', type=int, default=3, help='Количество лет ( > 0 )'
  )
  parser.add_argument(
      '--stores',
      type=int,
      default=5,
      help='Количество магазинов (не менее 5)',
  )
  parser.add_argument(
      '--out', type=str, default='data/sales.csv', help='Путь для сохранения CSV'
  )

  args = parser.parse_args()

  try:
    if args.years <= 0 or args.stores < 5 or not args.out:
      raise InvalidConfigError(
          'Некорректные параметры: годы должны быть > 0, магазинов >= 5, путь'
          ' обязателен.'
      )

    df = generate_sales_data(args.seed, args.years, args.stores)
    import os

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    df.to_csv(args.out, index=False)
    print(f'Успешно сгенерировано {len(df)} строк в файл {args.out}')

  except InvalidConfigError as e:
    print(f'Ошибка конфигурации: {e}', file=sys.stderr)
    sys.exit(1)
  except Exception as e:
    print(f'Произошла непредвиденная ошибка: {e}', file=sys.stderr)
    sys.exit(2)


if __name__ == '__main__':
  main()

