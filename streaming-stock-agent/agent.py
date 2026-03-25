from typing import Dict
import yfinance as yf


def _compare_stocks(symbol1: str, symbol2: str) -> Dict:
    try:
        stock1 = yf.Ticker(symbol1)
        stock2 = yf.Ticker(symbol2)

        price1 = stock1.info.get("currentPrice", "N/A")
        price2 = stock2.info.get("currentPrice", "N/A")

        return {
            "symbol1": symbol1,
            "price1": price1,
            "symbol2": symbol2,
            "price2": price2,
            "comparison": f"{symbol1}: {price1} vs {symbol2}: {price2}"
        }

    except Exception as e:
        return {"error": str(e)}


STOCK_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "compare_stocks",
            "description": "Compare two stock symbols and return their prices",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol1": {
                        "type": "string",
                        "description": "First stock symbol"
                    },
                    "symbol2": {
                        "type": "string",
                        "description": "Second stock symbol"
                    }
                },
                "required": ["symbol1", "symbol2"]
            }
        }
    }
]