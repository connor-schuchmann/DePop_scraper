import json
import statistics

# pull json to data
with open("listings.json", encoding="utf-8") as f:
    data = json.load(f)

# extract prices from data
prices = [listing["price"] for listing in data]

# statistical computations
count = len(prices)
mean = statistics.mean(prices)
median = statistics.median(prices)
low = min(prices)
high = max(prices)

print(f"Listings analyzed : {count}")
print(f"Average price     : ${mean:.2f}")
print(f"Median price      : ${median:.2f}")
print(f"Cheapest          : ${low:.2f}")
print(f"Most expensive    : ${high:.2f}")