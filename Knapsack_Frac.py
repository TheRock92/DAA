values = [60,20,100,120]
weights = [10,0,20,30]

capacity = 50

def fractional_knapsack(values, weights, W):

    n = len(values)
    items = []
    remaining = W
    total_value = 0.0
    fractions = [0.0]*n

    for i in range(n):
        if weights[i] == 0: # zero wieght item to first priority.
            if values[i] > 0:
                total_value += values[i]
                fractions[i] = 1.0
        else:
            items.append((values[i]/weights[i], i, values[i], weights[i]))



    items.sort(reverse=True)

    for ratio,i,v,w in items:
        if remaining<=0:
            break
        take = min(w,remaining)
        frac = take/w if w > 0 else 0.0
        fractions[i] = frac

        total_value += frac*v
        remaining -= take

    return total_value, fractions


max_val , fracs = fractional_knapsack(values, weights, capacity)

print("Maximum value in knapsack:", max_val)
print("Fractions of items taken:", fracs)

----------------------------------------------------------------------
# ---------- USER INPUT ----------
n = int(input("Enter number of items: "))
values = list(map(int, input(f"Enter {n} values separated by space: ").split()))
weights = list(map(int, input(f"Enter {n} weights separated by space: ").split()))
capacity = int(input("Enter knapsack capacity: "))
