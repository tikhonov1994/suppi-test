import numpy as np

from task5 import calculation_accumulated_percent


def assign_index():
    df = calculation_accumulated_percent()
    df['category'] = np.where(
        (df['accumulated_percent_profit_product_of_warehouse'] <= 70), 'A',
        np.where(
            (df['accumulated_percent_profit_product_of_warehouse'] <= 90),
            'B', 'C')
    )
    return df


if __name__ == '__main__':
    print(assign_index())
