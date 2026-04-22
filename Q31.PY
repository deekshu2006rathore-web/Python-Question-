import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate synthetic data using numpy
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
products = ['Product_A', 'Product_B', 'Product_C']

# Create random sales data: 6 months x 3 products
sales_data = np.random.randint(50, 200, size=(6, 3))

# 2. Create a pandas DataFrame
df = pd.DataFrame(sales_data, columns=products, index=months)
df['Total_Sales'] = df.sum(axis=1)  # Total sales per month

print("=== Sales Data (Units Sold) ===")
print(df)

# 3. Basic analysis with pandas
print("\n=== Summary Statistics ===")
print(df.describe())

print("\n=== Total Sales per Product ===")
print(df[products].sum())

print("\n=== Month with Highest Total Sales ===")
best_month = df['Total_Sales'].idxmax()
print(f"{best_month}: {df.loc[best_month, 'Total_Sales']} units")

# 4. Visualize with matplotlib
plt.figure(figsize=(12, 5))

# Subplot 1: Line chart - monthly sales per product
plt.subplot(1, 2, 1)
for product in products:
    plt.plot(df.index, df[product], marker='o', label=product)
plt.title('Monthly Sales by Product')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

# Subplot 2: Bar chart - total sales per product
plt.subplot(1, 2, 2)
total_per_product = df[products].sum()
plt.bar(total_per_product.index, total_per_product.values, color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Units')
plt.grid(axis='y', linestyle=':', alpha=0.7)

# Add value labels on bars
for i, v in enumerate(total_per_product.values):
    plt.text(i, v + 2, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Additional analysis: correlation between products
print("\n=== Correlation Matrix (Product Sales) ===")
print(df[products].corr())