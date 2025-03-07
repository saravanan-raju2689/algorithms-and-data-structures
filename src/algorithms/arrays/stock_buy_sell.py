def stock_buy_sell(prices):
    """
    Function to find the maximum profit from stock buy and sell.
    
    Parameters:
    prices (list): A list of stock prices where prices[i] is the price of a given stock on the ith day.
    
    Returns:
    tuple: A tuple containing the buy and sell days for maximum profit.
    """
    if not prices:
        return (None, None)

    min_price = float('inf')
    max_profit = 0
    buy_day = sell_day = 0

    for i in range(len(prices)):
        # Update min_price and buy_day
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        
        # Calculate profit and update sell_day
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
            sell_day = i

    if max_profit > 0:
        return (buy_day, sell_day)
    else:
        return (None, None)

# Example usage:
# prices = [7, 1, 5, 3, 6, 4]
# print(stock_buy_sell(prices))  # Output: (1, 4) -> Buy on day 1 and sell on day 4

"""
Big-O Analysis:
- Time Complexity: O(n), where n is the number of days (length of the prices list). 
  We traverse the list once to find the minimum price and maximum profit.
- Space Complexity: O(1), as we are using a constant amount of space for variables.
"""