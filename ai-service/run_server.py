#!/usr/bin/env python3
"""
Script to run the FastAPI server
"""
import uvicorn

if __name__ == "__main__":
    print("🚀 Starting Shopify AI Analytics Service...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔄 Auto-reload enabled for development")
    print("\n" + "="*50)
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
