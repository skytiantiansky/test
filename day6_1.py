import numpy as np
def get_max_profit(price):
    length=len(price)
    current_profit=[0]*length
    future_profit=[0]*length
    low=price[0]
    for i in range(1,length):
        low=np.minimum(low,price[i-1])
        current_profit[i]=np.maximum(current_profit[i-1],price[i]-low)
    high=price[length-1]
    for j in range(length-2,-1,-1):
        high=np.maximum(high,price[j+1])
        future_profit[i]=np.maximum(future_profit[j+1],high-price[j])

    max_profit=0
    for i in range(length):
        max_profit=np.maximum(max_profit,current_profit[i]+future_profit[i])
    return max_profit



def main():
    price = [12, 15, 14, 8, 11, 10, 12]
    result = get_max_profit(price)
    print(result)

if __name__ == '__main__':
    main()