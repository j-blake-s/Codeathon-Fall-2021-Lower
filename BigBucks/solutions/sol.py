
# https://www.section.io/engineering-education/greedy-algorithms/
def maximize_profit(price_list):
    if len(price_list) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')
    
    min_price = price_list[0]
    max_profit = price_list[1] - price_list[0]
    
    for day in range(1, len(price_list)):
        stock_price_current = price_list[day]
        tentative_profit = stock_price_current - min_price
        max_profit = max(max_profit, tentative_profit)
        min_price = min(min_price, stock_price_current)
    
    return max_profit

cases = int(input())
for _ in range(cases):
    n = int(input())
    m = [int(x) for x in input().split()]
    print(maximize_profit(m))
