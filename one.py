import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
try:
    df = pd.read_csv("restaurant_sales.csv")
    df2 = pd.read_csv("one_row.csv")
except FileNotFoundError:
    print("Error: restaurant_sales.csv not found.")
    raise SystemExit

# Check the required columns
required = ["Date", "Item", "Category", "Quantity", "Price"]

if not all(col in df.columns for col in required):
    print("Error: CSV file has missing columns.")
    raise SystemExit

# Convert quantity and price to numbers
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)
df["Price"] = pd.to_numeric(
    df["Price"], errors="coerce"
)

# Skip invalid rows
valid = (
    df["Quantity"].notna()
    & df["Price"].notna()
    & (df["Quantity"] >= 0)
    & (df["Price"] >= 0)
)

for i in df.index[~valid]:
    print(f"Warning: Row {i + 2} skipped.")

df = df[valid].copy()

# Calculate sales revenue
df["Sales"] = df["Quantity"] * df["Price"]

print("Valid rows read:", len(df))
print("Total sales: Rs.", df["Sales"].sum())

#Correct category names
df["Category"] = df["Category"].str.strip().str.title()

# Sales by category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by category:")
print(category_sales)

# Sales by date
daily_sales = df.groupby("Date")["Sales"].sum()
print("\nDaily sales:")
print(daily_sales)

# Top item by quantity
quantity_sales = df.groupby("Item")["Quantity"].sum()
top_quantity = quantity_sales.idxmax()
top_quantity_value =int(quantity_sales.max())

print("\nTop item by quantity:", top_quantity,
      f"({top_quantity_value} units)")

# Top item by revenue
df["Item"] = df["Item"].str.strip().str.title()

item_sales = df.groupby("Item")["Sales"].sum()

top_revenue = item_sales.idxmax()
top_revenue_value = item_sales.max()

print("Top item by revenue:", top_revenue,
      f"(Rs. {top_revenue_value})")

# Best sales day
best_day = daily_sales.idxmax()
print("Best day:", best_day,
      f"(Rs. {daily_sales[best_day]})")

# Create dashboard charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

category_sales.plot(
    kind="bar", ax=axes[0], title="Sales by Category"
)
axes[0].set_ylabel("Revenue (Rs.)")

daily_sales.plot(
    kind="line", marker="o", ax=axes[1],
    title="Daily Sales"
)
axes[1].set_ylabel("Revenue (Rs.)")

print("\n---Test Case 1,3,4 ---")
df = pd.read_csv("restaurant_sales.csv")

print("\n---Test Case 2 ---")
df2 = pd.read_csv("one_row.csv")
plt.tight_layout()
plt.show()