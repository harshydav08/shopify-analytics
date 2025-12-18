# AI Agent Pipeline
# Implements the 6-stage reasoning pipeline for Shopify analytics questions
from typing import Dict, List

from schemas import DataPoint, QuestionResponse
from shopify_mock import MockShopifyAPI


class ShopifyAIAgent:
    """
    AI Agent that processes natural language questions through a 6-stage pipeline:
    1. Intent Classification
    2. Planning (data source selection)
    3. ShopifyQL Generation
    4. Query Validation
    5. Execution (mocked)
    6. Business Explanation
    """

    def __init__(self) -> None:
        self.mock_api = MockShopifyAPI()

    def process_question(self, store_id: str, question: str) -> QuestionResponse:
        """Main pipeline orchestrator"""
        intent = self.classify_intent(question)
        if intent == "unknown":
            return QuestionResponse(
                answer="I can help with sales, inventory, or customers. Try asking about top products, stock levels, or customer stats.",
                confidence="low",
                query_generated="",
                data_points=[],
                intent=intent,
                error="Could not classify intent"
            )

        plan = self.plan_data_source(intent, question)
        query = self.generate_shopifyql(intent, plan)
        self.validate_query(query)

        executed = self.execute_query(query, store_id, intent)
        answer = self.explain_results(executed["data_points"], intent, store_id, question)

        data_points = [DataPoint(**dp) for dp in executed["data_points"]]

        return QuestionResponse(
            answer=answer,
            confidence=executed.get("confidence", "medium"),
            query_generated=query,
            data_points=data_points,
            intent=intent,
            error=executed.get("error")
        )

    def classify_intent(self, question: str) -> str:
        """Stage 1: Classify user intent (sales, inventory, customers)"""
        q = question.lower()
        if any(k in q for k in ["sale", "revenue", "top", "selling", "orders", "aov", "average order", "trend"]):
            return "sales"
        if any(k in q for k in ["inventory", "stock", "qty", "quantity", "out of stock", "reorder"]):
            return "inventory"
        if any(k in q for k in ["customer", "users", "cohort", "retention", "repeat", "churn"]):
            return "customers"
        return "unknown"

    def plan_data_source(self, intent: str, question: str) -> Dict[str, str]:
        """Stage 2: Decide what data sources are needed"""
        if intent == "sales":
            return {"dataset": "orders", "time_window": "last_7_days", "group_by": "product_title"}
        if intent == "inventory":
            return {"dataset": "products", "filter": "low_stock"}
        if intent == "customers":
            return {"dataset": "customers", "metric": "growth"}
        return {"dataset": "unknown"}

    def generate_shopifyql(self, intent: str, plan: Dict[str, str]) -> str:
        """Stage 3: Generate ShopifyQL query string"""
        dataset = plan.get("dataset", "")
        if intent == "sales":
            return (
                "SELECT product_title, SUM(quantity * price) as revenue "
                "FROM orders WHERE created_at >= '7 days ago' "
                "GROUP BY product_title ORDER BY revenue DESC LIMIT 5"
            )
        if intent == "inventory":
            return (
                "SELECT product_title, inventory_quantity "
                "FROM products WHERE inventory_quantity < 50 "
                "ORDER BY inventory_quantity ASC"
            )
        if intent == "customers":
            return (
                "SELECT COUNT(*) as total_customers, AVG(total_spent) as avg_order_value "
                "FROM customers"
            )
        return f"-- Unsupported intent for dataset {dataset}"

    def validate_query(self, query: str) -> None:
        """Stage 4: Basic validation of generated query"""
        if not query or not isinstance(query, str):
            raise ValueError("Generated query is invalid")
        if query.startswith("-- Unsupported"):
            raise ValueError("Intent not supported")

    def execute_query(self, query: str, store_id: str, intent: str) -> Dict[str, List[Dict[str, str]]]:
        """Stage 5: Execute query (using mock data)"""
        return self.mock_api.execute_query(query, store_id, intent)

    def explain_results(self, data_points: List[Dict[str, str]], intent: str, store_id: str, question: str) -> str:
        """Stage 6: Convert technical data to business language"""
        if not data_points:
            return f"No data found for {store_id} based on your question. Try widening the date range or checking another metric."

        if intent == "sales":
            top = data_points[0]
            return (
                f"Top products for {store_id}: {top['label']} leads with {top['value']}. "
                f"Overall, these are your best performers for the period referenced."
            )

        if intent == "inventory":
            low_stock = [dp for dp in data_points if "unit" in dp["value"] or "units" in dp["value"]]
            needs_attention = low_stock[:3] if low_stock else data_points[:3]
            labels = ", ".join(dp["label"] for dp in needs_attention)
            return f"Watch inventory for: {labels}. Reorder the lowest items soon to avoid stockouts."

        if intent == "customers":
            summary = ", ".join(f"{dp['label']}: {dp['value']}" for dp in data_points[:3])
            return f"Customer snapshot for {store_id}: {summary}. Steady growth with healthy average spend."

        return f"Here is what I found for {store_id}: {question}"
