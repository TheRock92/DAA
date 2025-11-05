# 0-1 Knapsack Problem using Dynamic Programming

def knapsack(W, wt, val, n):
    # Create a DP table with (n+1) rows and (W+1) columns
    dp = [[0 for x in range(W + 1)] for y in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0   # Base case
            elif wt[i - 1] <= w:
                # Include or exclude the current item
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]   # Exclude item

    return dp[n][W]


# Example
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)

max_value = knapsack(capacity, weights, values, n)
print("Maximum value that can be obtained =", max_value)
