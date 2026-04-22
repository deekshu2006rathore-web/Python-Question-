import pandas as pd

# Create a sample CSV file for demonstration
csv_content = """Name,Age,Score,Grade
Alice,20,85,A
Bob,22,90,A
Charlie,21,78,B
Diana,23,92,A
Eve,19,65,C
"""

with open("students.csv", "w") as f:
    f.write(csv_content)

# Read the CSV file into a DataFrame
df = pd.read_csv("students.csv")

# Display basic information
print("=== First 3 rows ===")
print(df.head(3))

print("\n=== Data types and non-null counts ===")
print(df.info())

print("\n=== Summary statistics (numeric columns) ===")
print(df.describe())

print("\n=== Mean Age ===")
print(df["Age"].mean())

print("\n=== Maximum Score ===")
print(df["Score"].max())

print("\n=== Grouped analysis: Average Score by Grade ===")
print(df.groupby("Grade")["Score"].mean())

print("\n=== Filtering: Students with Score > 80 ===")
high_scorers = df[df["Score"] > 80]
print(high_scorers)