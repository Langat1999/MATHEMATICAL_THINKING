#A greedy algorithm for the coin change problem always selects the largest coin value possible. Note that this method works optimally for many—but not all—coin systems.
#At each step, the algorithm selects the largest coin that doesn’t exceed the remaining amount, demonstrating a straightforward greedy approach to an optimization problem.
def greedy_coin_change(amount, coins):
    """
    Return a list of coins that add up to the given amount using a greedy strategy.
    Assumes the coins are sorted in descending order.
    """
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# Coin denominations (sorted descending)
coins = [25, 10, 5, 1]
amount = 68  # For example, 68 cents

change = greedy_coin_change(amount, coins)
print("Coins used for 68 cents (greedy):", change)