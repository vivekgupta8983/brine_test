import pandas as pd

def compute_monthly_revenue(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    monthly_revenue = df.groupby('month')['product_price'].sum()
    return monthly_revenue

def compute_product_revenue(df):
    product_revenue = df.groupby('product_name')['product_price'].sum()
    return product_revenue

def compute_customer_revenue(df):
    customer_revenue = df.groupby('customer_id')['product_price'].sum()
    return customer_revenue

def identify_top_customers(df):
    top_customers = df.groupby('customer_id')['product_price'].sum().nlargest(10)
    return top_customers

# Read the data from CSV file
try:
    df = pd.read_csv('orders.csv')
except FileNotFoundError:
    print("File 'orders.csv' not found.")
    exit(1)

# Compute total revenue generated by each month
monthly_revenue = compute_monthly_revenue(df)
print("Monthly Revenue:")
print(monthly_revenue)
print()

# Compute total revenue generated by each product
product_revenue = compute_product_revenue(df)
print("Product Revenue:")
print(product_revenue)
print()

# Compute total revenue generated by each customer
customer_revenue = compute_customer_revenue(df)
print("Customer Revenue:")
print(customer_revenue)
print()

# Identify top 10 customers by revenue generated
top_customers = identify_top_customers(df)
print("Top 10 Customers by Revenue:")
print(top_customers)
