r = [0.8, 0.95, 0.7, 0.9, 0.85]

n = len(r)
a = []

for i in range(n):
    a.append([r[i], i + 1])

a.sort()

print("Порядок продажи оборудования:")
for x in a:
    print(x[1], end=' ')
