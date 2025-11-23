from src.agents.bi_agents import create_all_agents

print("Testing Agent Creation...")
print("="*60)

# Create all agents
try:
    agents = create_all_agents()
    
    print("\n✅ Successfully created all agents:")
    print(f"  1. Controller: {agents['controller'].role}")
    print(f"  2. Interpreter: {agents['interpreter'].role}")
    print(f"  3. Analyst: {agents['analyst'].role}")
    print(f"  4. Visualizer: {agents['visualizer'].role}")
    print(f"  5. Reporter: {agents['reporter'].role}")
    
    print("\n" + "="*60)
    print("✅ All agents created successfully!")
    print("\nAgent Architecture:")
    print("  Controller → Manages workflow")
    print("  Interpreter → Parses questions")
    print("  Analyst → Calculates metrics")
    print("  Visualizer → Designs charts")
    print("  Reporter → Generates insights")
    
    print("\n🎯 Next: Building the workflow orchestration...")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nDebugging info:")
    import traceback
    traceback.print_exc()