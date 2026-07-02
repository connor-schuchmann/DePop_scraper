import json
import pandas as pd

# pull json to data
with open("listings.json", encoding="utf-8") as f:
    data = json.load(f)

# push data to panda
df = pd.DataFrame(data)
print("summary: ")
print(df["price"].describe().round(2))

# computations
mean = df["price"].mean()
std = df["price"].std()
deal = mean - std

deals = df[df["price"] < deal].sort_values("price")

# show deals        
print(f"\nThreshold: ${deal:.2f}")
print(f"Found {len(deals)} deal(s):\n")
print(deals[["price", "size", "url"]].to_string(index=False))