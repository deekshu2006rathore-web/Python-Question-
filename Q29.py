import pandas as pd

# Sample dataset
data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank'],
    'Salary': [50000, 72000, 68000, 52000, 61000, 75000, 59000, 54000],
    'Experience': [2, 5, 4, 3, 6, 7, 4, 2]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Filtering: Select rows where Salary > 60000
print("\n--- Employees with Salary > 60000 ---")
high_salary = df[df['Salary'] > 60000]
print(high_salary)

# 2. Filtering: IT department employees with Experience >= 5
print("\n--- IT employees with Experience >= 5 ---")
it_experienced = df[(df['Department'] == 'IT') & (df['Experience'] >= 5)]
print(it_experienced)

# 3. Grouping: Average salary by department
print("\n--- Average Salary by Department ---")
avg_salary_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_dept)

# 4. Grouping with multiple aggregates: min, max, mean salary by department
print("\n--- Salary Statistics by Department ---")
salary_stats = df.groupby('Department')['Salary'].agg(['min', 'max', 'mean', 'count'])
print(salary_stats)

# 5. Grouping by multiple columns: Department and Experience level
print("\n--- Average Salary by Department and Experience (grouped) ---")
# Create experience category
df['Exp_Level'] = pd.cut(df['Experience'], bins=[0, 3, 6, 10], labels=['Junior', 'Mid', 'Senior'])
grouped = df.groupby(['Department', 'Exp_Level'])['Salary'].mean()
print(grouped)

# 6. Using filter() on groups: Keep departments with average salary > 60000
print("\n--- Departments with average salary > 60000 ---")
high_avg_depts = df.groupby('Department').filter(lambda x: x['Salary'].mean() > 60000)
print(high_avg_depts['Department'].unique())