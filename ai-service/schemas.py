# Pydantic Schemas for API Request/Response Validation
from pydantic import BaseModel
from typing import List, Optional

class QuestionRequest(BaseModel):
    """
    Input schema for questions sent to the AI agent
    """
    store_id: str  # e.g., "demo-store.myshopify.com"
    question: str  # Natural language question

class DataPoint(BaseModel):
    """
    Individual data point in the response
    """
    label: str
    value: str
    metric_type: Optional[str] = None

class QuestionResponse(BaseModel):
    """
    Output schema for AI agent responses
    """
    answer: str  # Business-friendly explanation
    confidence: str  # "low", "medium", "high"
    query_generated: str  # The ShopifyQL query that was generated
    data_points: List[DataPoint]  # Structured data points
    intent: Optional[str] = None  # Classified intent
    error: Optional[str] = None  # Error message if something went wrong
