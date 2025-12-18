# FastAPI Main Server
# Entry point for the AI service that handles natural language questions
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from agent import ShopifyAIAgent
from schemas import QuestionRequest, QuestionResponse

app = FastAPI(title="Shopify AI Analytics Service", version="1.0.0")
agent = ShopifyAIAgent()


@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"status": "AI Service is running", "version": "1.0.0"}


@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """
    Main endpoint that processes natural language questions about Shopify data
    """
    try:
        return agent.process_question(request.store_id, request.question)
    except ValueError as exc:
        # Validation or unsupported intent
        error_response = QuestionResponse(
            answer=str(exc),
            confidence="low",
            query_generated="",
            data_points=[],
            intent="unknown",
            error=str(exc)
        )
        return JSONResponse(status_code=400, content=error_response.model_dump())
    except Exception as exc:  # pragma: no cover - safeguard
        error_response = QuestionResponse(
            answer="Something went wrong while processing your question.",
            confidence="low",
            query_generated="",
            data_points=[],
            intent="unknown",
            error=str(exc)
        )
        return JSONResponse(status_code=500, content=error_response.model_dump())
