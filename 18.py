S = ["Amazon", "Yahoo", "eBay", "Yahoo", "Yahoo", "Oracle"]
S2 = ["Yahoo", "eBay", "Yahoo", "Oracle"]

n = len(S)
m = len(S2)

i = 0
j = 0

while i < n and j < m:
    if S[i] == S2[j]:
        j += 1
    i += 1

if j == m:
    print("YES")
else:
    print("NO")
