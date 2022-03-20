import numpy as np
import pandas as pd

from task2 import DELIVERY_UNIT, get_summary_of_products


def get_warehouse_info(dict):
    df = pd.DataFrame.from_dict(dict, orient='index')
    df['profit'] = (df['warehouse_name'].transform(
        lambda x: DELIVERY_UNIT[x]) + df['price']) * df['quantity']
    df.drop(columns='price', inplace=True)
    res = df.groupby(['warehouse_name', 'product']).aggregate(
        np.sum).reset_index()
    res['sum'] = [res.loc[res['warehouse_name'] == v,
                          'profit'].sum() for v in res['warehouse_name']]
    res['percent_profit_product_of_warehouse'] = (
        res['profit'] / res['sum'] * 100)
    res.drop(columns='sum', inplace=True)
    return res


if __name__ == '__main__':
    print(get_warehouse_info(get_summary_of_products()))
