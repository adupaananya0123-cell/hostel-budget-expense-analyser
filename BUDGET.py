import pandas as pd
import numpy as np

budget = 5000

items = ["Food", "Travel", "Books", "Snacks", "Shopping"]
amounts = [1500, 500, 600, 400, 700]

data = {"Item": items, "Amount": amounts}
df = pd.DataFrame(data)

print("HOSTEL BUDGET ANALYZER")
print(df)

total = np.sum(amounts)
remaining = budget - total

print("Monthly Budget:", budget)
print("Total Expenses:", total)
print("Remaining Money:", remaining)

print("Highest Expense:", np.max(amounts))
print("Average Expense:", np.mean(amounts))

if remaining < 0:
    print("Budget Exceeded")
else:
    print("Budget is Within Limit")