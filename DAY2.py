import numpy as np
def get_max_profit(price):
    if len(price)==0 or price is None:
        return 0
    max_profit=0
    min_price=price[0]
    for i in range(1,len(price)):
        min_price=np.minimum(min_price,price[i])
        max_profit=np.maximum(max_profit,price[i]-min_price)
    return max_profit


def main():
    price = [12, 15, 14, 8, 11, 10, 12]
    result = get_max_profit(price)
    print(result)


if __name__ == '__main__':
    main()