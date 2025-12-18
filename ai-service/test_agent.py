#!/usr/bin/env python3
"""
Direct test of the AI Agent without requiring a running server
"""
from agent import ShopifyAIAgent

def test_agent():
    """Test the AI Agent directly"""
    print("=" * 60)
    print("Testing Shopify AI Agent (Direct)")
    print("=" * 60)
    
    agent = ShopifyAIAgent()
    store_id = "demo-store.myshopify.com"
    
    # Test 1: Sales question
    print("\n1. Testing Sales Question...")
    question = "What were my top selling products last week?"
    result = agent.process_question(store_id, question)
    print(f"   ✅ Intent: {result.intent}")
    print(f"   ✅ Confidence: {result.confidence}")
    print(f"   ✅ Answer: {result.answer}")
    print(f"   ✅ Query: {result.query_generated[:80]}...")
    print(f"   ✅ Data Points: {len(result.data_points)} items")
    for dp in result.data_points:
        print(f"      - {dp.label}: {dp.value}")
    
    # Test 2: Inventory question
    print("\n2. Testing Inventory Question...")
    question = "Show me low stock items"
    result = agent.process_question(store_id, question)
    print(f"   ✅ Intent: {result.intent}")
    print(f"   ✅ Confidence: {result.confidence}")
    print(f"   ✅ Answer: {result.answer}")
    print(f"   ✅ Data Points: {len(result.data_points)} items")
    for dp in result.data_points:
        print(f"      - {dp.label}: {dp.value}")
    
    # Test 3: Customer question
    print("\n3. Testing Customer Question...")
    question = "How many customers do I have?"
    result = agent.process_question(store_id, question)
    print(f"   ✅ Intent: {result.intent}")
    print(f"   ✅ Confidence: {result.confidence}")
    print(f"   ✅ Answer: {result.answer}")
    print(f"   ✅ Data Points: {len(result.data_points)} items")
    for dp in result.data_points:
        print(f"      - {dp.label}: {dp.value}")
    
    # Test 4: Unknown question
    print("\n4. Testing Unknown/Unsupported Question...")
    question = "What's the weather like?"
    result = agent.process_question(store_id, question)
    print(f"   ✅ Intent: {result.intent}")
    print(f"   ✅ Confidence: {result.confidence}")
    print(f"   ✅ Answer: {result.answer}")
    print(f"   ✅ Error: {result.error}")
    
    # Test 5: Different sales variations
    print("\n5. Testing Intent Classification Variations...")
    test_questions = [
        ("Show me revenue trends", "sales"),
        ("Check inventory quantity", "inventory"),
        ("Customer retention rate", "customers"),
        ("Average order value last month", "sales"),
        ("Products out of stock", "inventory"),
    ]
    
    for q, expected_intent in test_questions:
        detected_intent = agent.classify_intent(q)
        status = "✅" if detected_intent == expected_intent else "❌"
        print(f"   {status} '{q}' -> {detected_intent} (expected: {expected_intent})")
    
    print("\n" + "=" * 60)
    print("All agent tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    test_agent()
