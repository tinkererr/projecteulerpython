arr = []
n = 0

while (round((1 / (5 ** 0.5)) * ((1 + (5 ** 0.5)) / 2) ** (n+1))) <= 4000000:
    arr.append(round((1 / (5 ** 0.5)) * ((1 + (5 ** 0.5)) / 2) ** (n+1)))
    n += 1

print(sum([x for x in arr if x % 2 == 0]))
