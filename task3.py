import pandas as pd

data = pd.read_json('trial_task.json')


def get_total_income(data):
    res = 0
    for elem in data:
        res += (elem.get('quantity', 0) * elem.get('price', 0))
    return res


def find_order_profit(df):
    df['order_profit'] = df['highway_cost'] + df[
        'products'].transform(lambda x: get_total_income(x))
    print(df[['order_id', 'order_profit']])
    print('\nMean\n------')
    print(df['order_profit'].mean())


if __name__ == '__main__':
    find_order_profit(data)
