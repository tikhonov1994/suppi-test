from task2 import get_summary_of_products
from task4 import get_warehouse_info


def calculation_accumulated_percent():
    df = get_warehouse_info(get_summary_of_products())
    df.sort_values(['warehouse_name', 'percent_profit_product_of_warehouse'],
                   inplace=True, ascending=False)
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)
    df['accumulated_percent_profit_product_of_warehouse'] = (
        df.groupby('warehouse_name')[
            'percent_profit_product_of_warehouse'].cumsum())
    return df


if __name__ == '__main__':
    print(calculation_accumulated_percent())
