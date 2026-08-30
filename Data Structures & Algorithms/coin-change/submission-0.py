class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0 

        history = [-1] * (amount + 1)
        minCoin = 2**31
        
        for coin in coins:
            if coin <= amount: 
                history[coin] = 1
                minCoin = min(minCoin, coin)

        for i in range(minCoin + 1, amount + 1):
            for coin in coins:  
                if coin <= i and history[i - coin] != -1:
                    if history[i] == -1:
                        history[i] = history[i - coin] + 1
                    else:
                        history[i] = min(history[i], history[i - coin] + 1)
        return history[amount]
                    


        
