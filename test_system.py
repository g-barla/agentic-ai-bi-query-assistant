"""
Test the complete BI Query Assistant system with various queries.
"""

from src.main import BIQueryAssistant

# Create assistant
assistant = BIQueryAssistant()

# Test queries covering different scenarios
test_queries = [
    "What is our total revenue?",  
    "Show me the top 5 products by revenue",
    "What is our month-over-month growth rate?",
    "How many unique customers do we have?",
    "What was our Q1 revenue?"
]


print("TESTING BI QUERY ASSISTANT - MULTIPLE QUERIES")
print("="*80)

for i, query in enumerate(test_queries[:3], 1):  
    print(f"\n{'#'*80}")
    print(f"TEST {i}/3: {query}")
    print(f"{'#'*80}\n")
    
    try:
        result = assistant.process_query(query)
        print(f"\n✅ Test {i} completed successfully!")
    except Exception as e:
        print(f"\n❌ Test {i} failed: {e}")
    
    
    input("Press Enter to continue to next test...")


print("🎉 SYSTEM TESTING COMPLETE!")
