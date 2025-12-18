#!/usr/bin/env python3
"""
Simple test script to verify the FastAPI server works
"""
import requests
import json

def test_server():
    """Test the FastAPI server endpoints"""
    base_url = "http://localhost:8000"
    
    print("=" * 60)
    print("Testing Shopify AI Analytics Service")
    print("=" * 60)
    
    # Test health check
    print("\n1. Testing Health Check Endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"   ✅ Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   ❌ Health Check Failed: {e}")
        print("   Make sure the server is running: python run_server.py")
        return
    
    # Test sales question
    print("\n2. Testing Sales Question...")
    test_sales = {
        "store_id": "demo-store.myshopify.com",
        "question": "What were my top selling products last week?"
    }
    
    try:
        response = requests.post(f"{base_url}/ask", json=test_sales)
        print(f"   ✅ Status: {response.status_code}")
        result = response.json()
        print(f"   Intent: {result['intent']}")
        print(f"   Confidence: {result['confidence']}")
        print(f"   Answer: {result['answer']}")
        print(f"   Query: {result['query_generated'][:80]}...")
        print(f"   Data Points: {len(result['data_points'])} items")
    except Exception as e:
        print(f"   ❌ Sales Question Failed: {e}")
    
    # Test inventory question
    print("\n3. Testing Inventory Question...")
    test_inventory = {
        "store_id": "demo-store.myshopify.com",
        "question": "Show me low stock inventory items"
    }
    
    try:
        response = requests.post(f"{base_url}/ask", json=test_inventory)
        print(f"   ✅ Status: {response.status_code}")
        result = response.json()
        print(f"   Intent: {result['intent']}")
        print(f"   Confidence: {result['confidence']}")
        print(f"   Answer: {result['answer']}")
        print(f"   Data Points: {len(result['data_points'])} items")
    except Exception as e:
        print(f"   ❌ Inventory Question Failed: {e}")
    
    # Test customer question
    print("\n4. Testing Customer Question...")
    test_customer = {
        "store_id": "demo-store.myshopify.com",
        "question": "How many customers do I have?"
    }
    
    try:
        response = requests.post(f"{base_url}/ask", json=test_customer)
        print(f"   ✅ Status: {response.status_code}")
        result = response.json()
        print(f"   Intent: {result['intent']}")
        print(f"   Confidence: {result['confidence']}")
        print(f"   Answer: {result['answer']}")
        print(f"   Data Points: {len(result['data_points'])} items")
    except Exception as e:
        print(f"   ❌ Customer Question Failed: {e}")
    
    # Test unknown question
    print("\n5. Testing Unknown/Unsupported Question...")
    test_unknown = {
        "store_id": "demo-store.myshopify.com",
        "question": "What's the weather like today?"
    }
    
    try:
        response = requests.post(f"{base_url}/ask", json=test_unknown)
        print(f"   ✅ Status: {response.status_code}")
        result = response.json()
        print(f"   Intent: {result['intent']}")
        print(f"   Confidence: {result['confidence']}")
        print(f"   Answer: {result['answer']}")
    except Exception as e:
        print(f"   ❌ Unknown Question Failed: {e}")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    test_server()
