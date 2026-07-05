import pandas as pd

from ebay_client import get_access_token, search_listings
from listings import extract_listings

query = "airpods pro 2nd gen"  # what we are searching for

token = get_access_token()
results = search_listings(token, query)
data = extract_listings(results)

# push data to panda + show stats
df = pd.DataFrame(data)
print("summary: ")
print(df["total_price"].describe().round(2))

# computations
mean = df["total_price"].mean()
std = df["total_price"].std()
deal = mean - std

deals = df[df["total_price"] < deal].sort_values("total_price")

# show deals
print(f"\nThreshold: ${deal:.2f}")
print(f"Found {len(deals)} deal(s):\n")
print(deals[["title", "total_price", "condition", "url"]].to_string(index=False))