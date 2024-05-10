import pandas as pd

data = {
    "ice_cream_size" : [12,14,16,20,22,24,26,28],
    "ice_cream_price" : [20,28,36,44,52,60,68,76]
}
df = pd.DataFrame(data)
print(df)

df.to_csv("ice_cream_sales.csv",index=False)

print()

csv_data = pd.read_csv("ice_cream_sales.csv")
print(csv_data)