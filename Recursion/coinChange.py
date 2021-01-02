def coin_change(coins, amount):
    """Function for generating coin change."""
    if amount < 1:
        return 0
    return coin_change_recur(coins, amount, [0]*amount)


def coin_change_recur(coins, rem: int, count):
    if rem < 0:
        return -1
    if rem == 0:
        return 0
    if count[rem - 1] != 0:
        return count[rem - 1]
    min_val = float("inf")
    for coin in coins:
        res = coin_change_recur(coins, rem - coin, count)
        if res >= 0 and res < min_val:
            min_val = 1 + res
    if min_val == float("inf"):
        count[rem - 1] = -1
    else:
        count[rem - 1] = min_val
    return count[rem - 1]


print(coin_change(coins=[1, 2, 5], amount=11))