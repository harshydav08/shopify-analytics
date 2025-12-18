# 🛍️ Shopify AI Analytics App

> An AI-powered analytics system that understands natural language questions about Shopify store data and provides business-friendly insights.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![Ruby on Rails](https://img.shields.io/badge/Rails-API-red.svg)](https://rubyonrails.org/)

## 🎯 Project Overview

This application allows Shopify store owners to ask questions in plain English and receive actionable insights with structured data. The system uses a **6-stage AI reasoning pipeline** to process queries and generate business-friendly responses.

**Example Queries:**
- "What were my top selling products last week?"
- "Show me items that are low on stock"
- "How many customers do I have?"

## 🏗️ Architecture

```
User Question → Rails API Gateway → Python AI Agent → Mock Shopify API → Response
                                          ↓
                                 6-Stage Pipeline:
                                 1. Intent Classification
                                 2. Planning
                                 3. ShopifyQL Generation
                                 4. Query Validation
                                 5. Execution (Mocked)
                                 6. Business Explanation
```

## 📁 Project Structure

```
shopify-ai-analytics/
├── ai-service/                    # Python FastAPI AI Service
│   ├── agent.py                  # 6-stage reasoning pipeline
│   ├── main.py                   # FastAPI server with /ask endpoint
│   ├── shopify_mock.py           # Mock Shopify API responses
│   ├── schemas.py                # Pydantic data models
│   ├── requirements.txt          # Python dependencies
│   ├── run_server.py             # Server launcher
│   ├── test_agent.py             # Direct agent tests
│   ├── test_server.py            # HTTP API tests
│   └── demo.py                   # Usage examples
│
├── rails-api/                     # Ruby on Rails API Gateway
│   └── app/controllers/api/v1/
│       └── questions_controller.rb  # Forwards to Python service
│
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- pip & virtualenv
- (Optional) Ruby on Rails for gateway

### 1. Set Up Python AI Service

```bash
cd ai-service

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start the server
python run_server.py
```

The API will be available at `http://localhost:8000`

### 2. Test the Service

```bash
# Run direct agent tests
python test_agent.py

# See usage examples
python demo.py
```

### 3. Use the API

**Via Python:**
```python
import requests

response = requests.post(
    "http://localhost:8000/ask",
    json={
        "store_id": "my-store.myshopify.com",
        "question": "What are my top selling products?"
    }
)
print(response.json())
```

**Via cURL:**
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "store_id": "my-store.myshopify.com",
    "question": "Show me low stock items"
  }'
```

**Interactive API Docs:**
Visit `http://localhost:8000/docs` for auto-generated Swagger UI

## 🧠 How It Works

### The 6-Stage Pipeline

1. **Intent Classification**: Categorizes questions as sales, inventory, or customer queries
2. **Planning**: Determines what data sources are needed
3. **ShopifyQL Generation**: Creates SQL-like queries for Shopify data
4. **Query Validation**: Ensures generated queries are valid
5. **Execution**: Runs queries against mock Shopify API
6. **Business Explanation**: Converts technical results to human-friendly insights

### Supported Question Types

| Category | Example Questions |
|----------|------------------|
| 📊 **Sales** | "Top selling products", "Revenue trends", "Average order value" |
| 📦 **Inventory** | "Low stock items", "Items to reorder", "Out of stock products" |
| 👥 **Customers** | "Total customers", "Customer growth", "New customers this week" |

## 🧪 Testing

**Direct Agent Tests:**
```bash
python test_agent.py
```

**HTTP API Tests:**
```bash
# Ensure server is running first
python test_server.py
```

**All tests include:**
- ✅ Intent classification accuracy
- ✅ Query generation correctness
- ✅ Mock data validation
- ✅ Error handling verification

## 📊 API Response Format

```json
{
  "answer": "Top products for my-store: iPhone Cases leads with $2,450...",
  "confidence": "medium",
  "query_generated": "SELECT product_title, SUM(quantity * price)...",
  "data_points": [
    {
      "label": "iPhone Cases",
      "value": "$2,450",
      "metric_type": "revenue"
    }
  ],
  "intent": "sales",
  "error": null
}
```

## 🔧 Configuration

**Environment Variables:**
- `AI_SERVICE_URL`: Python service URL (default: `http://127.0.0.1:8000/ask`)

## 🚧 Future Enhancements

- [ ] Replace rule-based classification with ML model
- [ ] Integrate with real Shopify API
- [ ] Add authentication & rate limiting
- [ ] Implement caching layer (Redis)
- [ ] Add query history and analytics
- [ ] Support more complex queries
- [ ] Deploy to production (Docker + Kubernetes)

## 📝 Implementation Status

- ✅ Project structure created
- ✅ FastAPI server implemented
- ✅ 6-stage AI pipeline built
- ✅ Intent classification added
- ✅ ShopifyQL generation implemented
- ✅ Mock data responses working
- ✅ Business explanation layer complete
- ✅ Rails API gateway functional
- ✅ Error handling added
- ✅ Tests and demos created
- ✅ Documentation finalized

## 🤝 Contributing

This is a demonstration project. For production use, consider:
- Adding proper authentication
- Implementing real Shopify API integration
- Training ML models on real query data
- Adding comprehensive test coverage
- Setting up CI/CD pipelines

## 📄 License

This project is for educational and demonstration purposes.

## 👤 Author

Built as part of Shopify AI Analytics assignment

---

**Questions or feedback?** Feel free to open an issue or reach out!
