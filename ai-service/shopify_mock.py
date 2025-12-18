# Mock Shopify API Executor
# Simulates Shopify API responses with realistic hardcoded data
from typing import Dict, List


class MockShopifyAPI:
    """
    Mock implementation of Shopify API that returns realistic but hardcoded data
    Simulates different scenarios including empty results
    """

    def execute_query(self, query: str, store_id: str, intent: str) -> Dict[str, List[Dict[str, str]]]:
        """
        Execute a ShopifyQL query and return mocked realistic data
        """
        intent = intent or "unknown"

        if intent == "sales":
            return {"data_points": self._get_mock_sales_data(), "confidence": "medium", "error": None}
        if intent == "inventory":
            return {"data_points": self._get_mock_inventory_data(), "confidence": "high", "error": None}
        if intent == "customers":
            return {"data_points": self._get_mock_customer_data(), "confidence": "medium", "error": None}

        return self._simulate_empty_results()

    def _get_mock_sales_data(self) -> List[Dict[str, str]]:
        """Mock sales data for top products queries"""
        return [
            {"label": "iPhone Cases", "value": "$2,450", "metric_type": "revenue"},
            {"label": "Coffee Mugs", "value": "$1,890", "metric_type": "revenue"},
            {"label": "T-shirts", "value": "$1,650", "metric_type": "revenue"},
        ]

    def _get_mock_inventory_data(self) -> List[Dict[str, str]]:
        """Mock inventory data for stock level queries"""
        return [
            {"label": "T-shirts", "value": "8 units", "metric_type": "inventory"},
            {"label": "iPhone Cases", "value": "12 units", "metric_type": "inventory"},
            {"label": "Coffee Mugs", "value": "45 units", "metric_type": "inventory"},
        ]

    def _get_mock_customer_data(self) -> List[Dict[str, str]]:
        """Mock customer data for customer analysis queries"""
        return [
            {"label": "Total Customers", "value": "245", "metric_type": "count"},
            {"label": "New This Week", "value": "23", "metric_type": "count"},
            {"label": "Average Order Value", "value": "$67", "metric_type": "currency"},
        ]

    def _simulate_empty_results(self) -> Dict[str, List[Dict[str, str]]]:
        """Simulate scenarios where no data is found"""
        return {"data_points": [], "confidence": "low", "error": "No data found"}
