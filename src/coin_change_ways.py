"""
Find the number of ways to make change for a given amount using given coin denominations.
"""

def count_coin_change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(count_coin_change(amount, coins))  # Output: 4