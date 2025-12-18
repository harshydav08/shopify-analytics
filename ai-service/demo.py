#!/usr/bin/env python3
"""
Demo script showing how to use the Shopify AI Analytics Service
"""
import sys

def demo_direct_usage():
    """Demo: Using the agent directly (without HTTP)"""
    print("\n" + "=" * 70)
    print("DEMO 1: Direct Agent Usage (Python)")
    print("=" * 70)
    
    from agent import ShopifyAIAgent
    
    agent = ShopifyAIAgent()
    store_id = "my-awesome-store.myshopify.com"
    
    # Example questions
    questions = [
        "What are my top 5 selling products?",
        "Show me items that are low on stock",
        "How many customers do I have?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n{i}. Question: '{question}'")
        result = agent.process_question(store_id, question)
        print(f"   Intent: {result.intent}")
        print(f"   Answer: {result.answer}")
        print(f"   Data: {len(result.data_points)} data points")

def demo_api_usage():
    """Demo: Using the API endpoint (requires server running)"""
    print("\n" + "=" * 70)
    print("DEMO 2: API Usage (HTTP)")
    print("=" * 70)
    print("\nTo use the API, first start the server:")
    print("  $ python run_server.py")
    print("\nThen send POST requests to http://localhost:8000/ask")
    print("\nExample with curl:")
    print('''
  curl -X POST http://localhost:8000/ask \\
    -H "Content-Type: application/json" \\
    -d '{
      "store_id": "my-store.myshopify.com",
      "question": "What were my top selling products?"
    }'
    ''')
    
    print("\nExample with Python requests:")
    print('''
  import requests
  
  response = requests.post(
      "http://localhost:8000/ask",
      json={
          "store_id": "my-store.myshopify.com",
          "question": "Show me low stock items"
      }
  )
  print(response.json())
    ''')

def demo_rails_gateway():
    """Demo: Using via Rails API Gateway"""
    print("\n" + "=" * 70)
    print("DEMO 3: Rails Gateway Usage")
    print("=" * 70)
    print("\n1. Start the Python AI service:")
    print("   $ cd ai-service && python run_server.py")
    print("\n2. Start the Rails server:")
    print("   $ cd rails-api && rails s")
    print("\n3. Send requests to Rails gateway:")
    print('''
  curl -X POST http://localhost:3000/api/v1/questions \\
    -H "Content-Type: application/json" \\
    -d '{
      "store_id": "my-store.myshopify.com",
      "question": "How many customers do I have?"
    }'
    ''')

def show_supported_questions():
    """Show examples of supported questions"""
    print("\n" + "=" * 70)
    print("Supported Question Types")
    print("=" * 70)
    
    print("\n📊 SALES Questions:")
    print("  • What were my top selling products?")
    print("  • Show me revenue trends")
    print("  • What's my average order value?")
    print("  • Top 5 products last week")
    
    print("\n📦 INVENTORY Questions:")
    print("  • Show me low stock items")
    print("  • Which products need reordering?")
    print("  • Check inventory levels")
    print("  • Items out of stock")
    
    print("\n👥 CUSTOMER Questions:")
    print("  • How many customers do I have?")
    print("  • Customer growth rate")
    print("  • What's my customer retention?")
    print("  • New customers this week")

if __name__ == "__main__":
    print("\n" + "🎯 " * 20)
    print("Shopify AI Analytics Service - Demo & Usage Guide")
    print("🎯 " * 20)
    
    # Run direct demo
    demo_direct_usage()
    
    # Show API usage
    demo_api_usage()
    
    # Show Rails gateway usage
    demo_rails_gateway()
    
    # Show supported questions
    show_supported_questions()
    
    print("\n" + "=" * 70)
    print("For more info, visit: http://localhost:8000/docs (when server running)")
    print("=" * 70 + "\n")
