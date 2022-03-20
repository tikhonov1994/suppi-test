import json

import numpy as np
import pandas as pd

DELIVERY_UNIT = {
    'Мордор': -10.0,
    'хутор близ Диканьки': -15.0,
    'отель Лето': -25.0,
    'остров невезения': -5.0,
    'гиперборея': -20.0
}


def get_summary_of_products():
    with open('trial_task.json') as json_file:
        data = json.load(json_file)
        iterator = 0
        output_data = {}
        for elem in data:
            for p in elem['products']:
                output_data[iterator] = {
                    'warehouse_name': elem['warehouse_name']}
                output_data[iterator]['product'] = p['product']
                output_data[iterator]['price'] = p['price']
                output_data[iterator]['quantity'] = p['quantity']
                iterator += 1
    return output_data


def find_sales_info(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df['delivery_cost'] = df['warehouse_name'].transform(
        lambda x: DELIVERY_UNIT[x]) * df['quantity']
    res = pd.pivot_table(df, index='product',
                         values=['price', 'quantity', 'delivery_cost'],
                         aggfunc=np.sum)
    res['total_profit'] = res['price'] + res['delivery_cost']
    res.rename(columns={'delivery_cost': 'total_divergence',
                        'price': 'total_income'}, inplace=True)
    print(res)


if __name__ == '__main__':
    find_sales_info(get_summary_of_products())
