import time
from main import Generate
import greedy

n = [10,100,1000,2000]
for i in n:
    cities = Generate(i)
    visited = set()
    before = round(time.time_ns() / (10**9), 10)
    result = greedy.main(cities, visited)
    after = round(time.time_ns() / (10**9), 10)
    print("Cities:\n", cities)
    print("Result:", result)
    print("N", i, ":", str(after-before) + "s")