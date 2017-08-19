factors = lambda x: [y for y in reversed(range(2,round(x/2)+1)) if x % y == 0 and len(factors(y)) == 0]
print(factors(600851475143)[0])
