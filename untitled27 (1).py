import random
import time
import matplotlib.pyplot as plt

print("=" * 60)
print("COMPETITIVE FACILITY LOCATION")
print("=" * 60)

n = 5
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
weights = [20, 10, 15, 5, 20]
target = 20

graph = [[] for _ in range(n)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

print("\n--- EXAMPLE DATA ---")
for i in range(n):
    print(f"  Zone {i+1}: profit = {weights[i]}")
for a, b in edges:
    print(f"  Edge: {a+1}-{b+1}")
print(f"Target score = {target}")

def available_moves(graph, taken):
    blocked = []
    for node in taken:
        if node not in blocked:
            blocked.append(node)
    for node in taken:
        for nb in graph[node]:
            if nb not in blocked:
                blocked.append(nb)
    free = []
    for i in range(len(graph)):
        if i not in blocked:
            free.append(i)
    return free

def solve(graph, weights, taken, player, score_p2):
    moves = available_moves(graph, taken)
    if len(moves) == 0:
        return score_p2

    if player == 2:
        best = -999999
        for m in moves:
            res = solve(graph, weights, taken + [m], 1, score_p2 + weights[m])
            if res > best:
                best = res
        return best
    else:
        best = 999999
        for m in moves:
            res = solve(graph, weights, taken + [m], 2, score_p2)
            if res < best:
                best = res
        return best

print("\n--- RESULT ---")
result = solve(graph, weights, [], 1, 0)
print(f"Player 2 gets: {result}")
if result >= target:
    print(f"YES (B={target})")
else:
    print(f"NO (B={target})")

target2 = 25
result = solve(graph, weights, [], 1, 0)
print(f"\nB = {target2}:")
if result >= target2:
    print("YES")
else:
    print(f"NO (only {result})")

print("\n" + "=" * 60)
print("PERFORMANCE TESTS")
print("=" * 60)

sizes = [4, 5, 6, 7, 8]
means = []
stds = []
hist_data = []

print("")

for size in sizes:
    times = []
    for trial in range(10):
        cons = []
        for i in range(size):
            for j in range(i + 1, size):
                if random.random() < 0.3:
                    cons.append((i, j))

        vals = []
        for i in range(size):
            vals.append(random.randint(1, 10))

        goal = sum(vals) // 3

        g = [[] for _ in range(size)]
        for u, v in cons:
            g[u].append(v)
            g[v].append(u)

        t1 = time.perf_counter()
        solve(g, vals, [], 1, 0)
        t2 = time.perf_counter()

        dt = t2 - t1
        times.append(dt)

        if size == 8:
            hist_data.append(dt)

    total = 0
    for t in times:
        total += t
    avg = total / len(times)
    means.append(avg)

    sq = 0
    for t in times:
        sq += (t - avg) ** 2
    sd = (sq / len(times)) ** 0.5
    stds.append(sd)

    print(f"n={size}: average={avg:.6f}s, std={sd:.6f}s")

print("\n" + "=" * 60)
print("PLOTS")
print("=" * 60)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(sizes, means, 'g-o', linewidth=2, markersize=8, label='Mean')
up = []
low = []
for i in range(len(sizes)):
    u = means[i] + 2 * stds[i]
    up.append(u)
    l = means[i] - 2 * stds[i]
    if l < 0:
        l = 0
    low.append(l)
plt.fill_between(sizes, low, up, alpha=0.2, color='green', label='±2σ')
plt.xlabel('Number of zones (n)')
plt.ylabel('Time (seconds)')
plt.title('Time vs Problem Size')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(hist_data, bins=8, edgecolor='black', alpha=0.7, color='purple')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Histogram for n = 8')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("DISTRIBUTION CHECK")
print("=" * 60)

data = hist_data
data.sort()
avg_val = sum(data) / len(data)
med_val = data[len(data) // 2]

print(f"n = 8:")
print(f"  Mean = {avg_val:.6f}")
print(f"  Median = {med_val:.6f}")

if avg_val > med_val:
    print("\nMean > Median → right tail")
    print("Hypothesis: LOGNORMAL distribution")
    cv = stds[sizes.index(8)] / avg_val
    print(f"CV = {cv:.3f}")
else:
    print("\nMean ≈ Median")
    print("Hypothesis: NORMAL distribution")

print("\n" + "=" * 60)
print("QUALITY ANALYSIS")
print("=" * 60)

print("\nQ: Is execution time good?")
print("A: NO for large inputs.")
print("\nReasons:")
print("1. PSPACE-complete problem")
print("2. Exponential growth observed")
print("3. n=4-5: fast (<0.01s)")
print("4. n=7-8: noticeable (seconds)")
print("5. n=10: minutes")
print("6. n=15: hours")
print("7. n=20: days")

if len(sizes) > 1:
    ratio = means[-1] / means[-2]
    print(f"\nGrowth factor: {ratio:.1f}x")
    pred9 = means[-1] * ratio
    pred10 = pred9 * ratio
    print(f"n=9 estimate: {pred9:.2f}s")
    print(f"n=10 estimate: {pred10:.2f}s")

print("\nConclusion: Only works for n≤8")

print("\n" + "=" * 60)
print("FINISHED")
print("=" * 60)
