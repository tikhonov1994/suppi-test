import pandas as pd

data = pd.read_json('trial_task.json')


def counting(data):
    res = 0
    for elem in data:
        res += elem.get('quantity', 0)
    return res


def find_shipping_cost(df):
    df['shipping_cost'] = df['highway_cost'] / df[
        'products'].transform(lambda x: counting(x))
    res = df[['warehouse_name', 'shipping_cost']].drop_duplicates()
    print(res)


if __name__ == '__main__':
    find_shipping_cost(data)
