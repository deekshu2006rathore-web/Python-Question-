import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 135, 150, 170, 160, 185]
expenses = [100, 110, 125, 140, 135, 150]

# ----- Line Graph -----
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Sales')
plt.plot(months, expenses, marker='s', linestyle='--', color='r', label='Expenses')
plt.title('Line Graph: Sales vs Expenses')
plt.xlabel('Months')
plt.ylabel('Amount (in $1000)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

# ----- Bar Graph -----
plt.subplot(1, 2, 2)  # 2nd subplot
plt.bar(months, sales, color='skyblue', edgecolor='black', label='Sales')
plt.bar(months, expenses, bottom=sales, color='lightcoral', edgecolor='black', label='Expenses (stacked)')
# Alternatively, side-by-side bars (uncomment below and comment above for side-by-side)
# x = range(len(months))
# width = 0.35
# plt.bar(x, sales, width, label='Sales', color='skyblue')
# plt.bar([i + width for i in x], expenses, width, label='Expenses', color='lightcoral')
# plt.xticks([i + width/2 for i in x], months)

plt.title('Bar Graph: Sales and Expenses')
plt.xlabel('Months')
plt.ylabel('Amount (in $1000)')
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()