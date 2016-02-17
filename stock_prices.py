# https://www.interviewcake.com/question/python/stock-price
import sys


def get_max_profit(prices):
    if len(prices) < 2:
        raise IndexError("Can't make a profit with fewer than 2 prices")
    min_price = sys.maxsize
    max_profit = 0

    for i in range(0, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_profit = max(max_profit, prices[i] - min_price)

    return max_profit

if __name__ == "__main__":
    stock_prices_yesterday = [10, 7]
    print(get_max_profit(stock_prices_yesterday))
