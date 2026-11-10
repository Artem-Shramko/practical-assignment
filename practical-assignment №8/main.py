                                       #Task 8.1
prices = [10, 50, 20, 80, 30, 90]
window_size = 3

max_profit = 0

for i in range(len(prices) - window_size + 1):
    current_min = prices[i]
    current_max = prices[i]
    for j in range(i, i + window_size):
        if prices[j] < current_min:
            current_min = prices[j]
        if prices[j] > current_max:
            current_max = prices[j]

    profit = current_max - current_min
    if profit > max_profit:
        max_profit = profit

print(f"Максимальний прибуток {window_size}: {max_profit}")
                                         #Task 8.2
consumption = [10, 5, 20, 15, 30, 25, 40]
queries = [(0, 2), (1, 4), (3, 6)]

prefix_sums = [0] * (len(consumption) + 1)
for i in range(len(consumption)):
    prefix_sums[i + 1] = prefix_sums[i] + consumption[i]

print("Динаміка споживання енергії за вибраними інтервалами:")
for start, end in queries:
    total_period_consumption = prefix_sums[end + 1] - prefix_sums[start]
    print(f"Інтервал від {start} по {end}: {total_period_consumption} одиниць")
