

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List

"""
Simple: 
Find profit maximizing function
BUt its two pointers algorithm solution
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.two_pointers(prices)


    def two_pointers(self,prices:List[int])->int:
        left,right = 0,1
        max_profit = 0
        while right < len(prices):
            buy_price = prices[left]
            sell_price = prices[right]
            if buy_price < sell_price:
                profit = sell_price-buy_price
                max_profit = max(max_profit,profit)
            else:
                ## Careful here we found minimum price
                left = right
            right+=1
        return max_profit


    def simple_efficient(self,prices:List[int])->int:
        # nested two foor loops is inefficient
        # lets slice array from current price to the future and get max value, instead of

        max_profit = 0
        for index_buy in range(len(prices)):
            buy_price = prices[index_buy]
            if index_buy+1 < len(prices):
                max_sell_price = max(prices[index_buy+1:])
                if max_sell_price > buy_price and max_sell_price-buy_price > max_profit:
                    max_profit = max_sell_price-buy_price
        return max_profit

    def simple(self,prices:List[int])-> int:
        # lets try brute force
        ## works but TIME LIMIT EXCEEDED
        max_profit = 0
        for index_buy in range(len(prices)):
            buy_price = prices[index_buy]
            for index_sell in range(index_buy+1,len(prices)):
                sell_price = prices[index_sell]
                if sell_price > buy_price:
                    if sell_price -buy_price > max_profit:
                        max_profit = sell_price-buy_price
        return max_profit

if __name__ == '__main__':
    prices = [1,2,4,2,5,7,2,4,9,0,2]
    print(Solution().maxProfit(prices))

