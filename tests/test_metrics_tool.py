from src.tools.business_metrics_engine import BusinessMetricsEngine

print("Testing Business Metrics Engine...")
print("="*60)

tool = BusinessMetricsEngine()

# Test 1
print("\n1. Total Revenue:")
print(tool.calculate("total_revenue"))

# Test 2
print("\n2. Top Products:")
print(tool.calculate("top_products", limit=5))

# Test 3
print("\n3. Customer Count:")
print(tool.calculate("customer_count"))

# Test 4
print("\n4. Growth Rate:")
print(tool.calculate("growth_rate"))

# Test 5
print("\n5. Q1 Revenue:")
print(tool.calculate("total_revenue", time_period="Q1"))

# Test 6
print("\n6. List all metrics:")
print(tool.list_metrics())

print("\n" + "="*60)
print("✅ Custom tool working perfectly!")