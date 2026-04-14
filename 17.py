r = [1.2, 1.5, 1.1, 1.8, 1.3]

n = len(r)
a = []

for i in range(n):
    a.append([r[i], i + 1])

a.sort(reverse=True)

print("Порядок покупки лицензий:")
for x in a:
    print(x[1], end=' ')
