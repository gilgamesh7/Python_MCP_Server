import asyncio

from mcp.server.fastmcp import FastMCP
from transactional_db import CUSTOMERS_TABLE, ORDERS_TABLE, PRODUCTS_TABLE

mcp = FastMCP("ecommerce_tools")

@mcp.tool
async def get_customer_info(customer_id: str) -> str:
    """Search for a customer using their unique identifier"""

    customer_info = CUSTOMERS_TABLE.get(customer_id, None)
    if not customer_info:
        return "Customer not found."
    
    return str(customer_info)