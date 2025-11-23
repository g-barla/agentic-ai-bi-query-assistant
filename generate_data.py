import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Generating sample sales data...")
print("="*60)

# Set random seed for reproducibility
np.random.seed(42)

# Generate dates for entire year 2024
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]

# Define business data
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
regions = ['North', 'South', 'East', 'West']
channels = ['Online', 'Retail', 'Partner']

# Product price ranges 
product_prices = {
    'Laptop': (800, 2000),
    'Monitor': (200, 800),
    'Keyboard': (30, 150),
    'Mouse': (15, 80),
    'Headphones': (50, 300)
}

# Generate 1000 sales transactions
num_transactions = 1000
data = []

for i in range(num_transactions):
    product = np.random.choice(products)
    price_range = product_prices[product]
    
    transaction = {
        'transaction_id': f'TXN{i+1:04d}',
        'date': np.random.choice(dates),
        'product': product,
        'region': np.random.choice(regions),
        'channel': np.random.choice(channels),
        'quantity': np.random.randint(1, 10),
        'unit_price': round(np.random.uniform(price_range[0], price_range[1]), 2),
        'customer_id': f'CUST{np.random.randint(1000, 5000):04d}'
    }
    
    # Calculate revenue
    transaction['revenue'] = round(transaction['quantity'] * transaction['unit_price'], 2)
    
    data.append(transaction)

# Create DataFrame
df = pd.DataFrame(data)

# Add useful columns
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['quarter'] = df['date'].dt.quarter
df['month_name'] = df['date'].dt.strftime('%B')

# Sort by date
df = df.sort_values('date').reset_index(drop=True)

# Save to CSV
df.to_csv('data/sample_sales_data.csv', index=False)

print(f"\n✅ Generated {len(df)} transactions")
print(f"✅ Date range: {df['date'].min().date()} to {df['date'].max().date()}")
print(f"✅ Total revenue: ${df['revenue'].sum():,.2f}")
print(f"✅ Products: {', '.join(products)}")
print(f"✅ Regions: {', '.join(regions)}")
print(f"\n📁 Data saved to: data/sample_sales_data.csv")

# Show sample
print("\nSample data (first 5 rows):")
print(df.head().to_string())

print("🎉 Data generation complete!")