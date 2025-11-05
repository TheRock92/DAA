# ---------- FRACTIONAL KNAPSACK ----------

def fractional_knapsack(values, weights, capacity):
    n = len(values)
    # Compute value/weight ratio
    ratio = [(values[i]/weights[i], weights[i], values[i]) for i in range(n)]
    
    # Sort items by ratio in descending order
    ratio.sort(reverse=True)
    
    total_value = 0.0
    for r, w, v in ratio:
        if capacity == 0:
            break
        if w <= capacity:
            # Take full item
            total_value += v
            capacity -= w
        else:
            # Take fraction of item
            total_value += r * capacity
            capacity = 0
    return total_value

# ---------- MAIN ----------
n = int(input("Enter number of items: "))
values = list(map(int, input("Enter values separated by space: ").split()))
weights = list(map(int, input("Enter weights separated by space: ").split()))
capacity = int(input("Enter knapsack capacity: "))

max_value = fractional_knapsack(values, weights, capacity)
print("Maximum value that can be taken in knapsack:", round(max_value, 2))

