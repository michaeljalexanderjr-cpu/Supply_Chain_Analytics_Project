import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Calculate profit
df["Profit"] = df["Revenue"] - df["Cost"]

# KPI calculations
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
avg_margin = (df["Profit"] / df["Revenue"]).mean()

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Average Margin:", round(avg_margin, 2))

# Regional Summary
regional_summary = df.groupby("Region")[["Revenue", "Profit"]].sum()
print("\nRegional Performance:")
print(regional_summary)
