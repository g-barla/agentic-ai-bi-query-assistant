from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print("Testing OpenAI API...")
print("="*60)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Cheaper, faster
        messages=[{"role": "user", "content": "Say 'OpenAI API works!'"}],
        temperature=0.1
    )
    
    print(f"\n✅ {response.choices[0].message.content}")
    print("\n" + "="*60)
    print("🎉 Ready to build!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure you:")
    print(" Copied correct API key")