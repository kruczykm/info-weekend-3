from pricing import calculate_total_revenue

def print_revenue_report(total_revenue: float):
    print("Retail revenue report")
    print(f"Total revenue: {total_revenue:.2f}.") # zaograglamy do dwoch miejsc po przecinku

# orders_raw = [
#     {"invoice_no": "536365", "stock_code": "85123A", "description": "WHITE HANGING HEART T-LIGHT HOLDER", "quantity": "6", "unit_price": "2.55", "customer_id": "17850", "country": "United Kingdom"},
#     {"invoice_no": "536366", "stock_code": "71053", "description": "WHITE METAL LANTERN", "quantity": "-1", "unit_price": "3.39", "customer_id": "17850", "country": "United Kingdom"},
#     {"invoice_no": "536367", "stock_code": "84406B", "description": "CREAM CUPID HEARTS COAT HANGER", "quantity": "8", "unit_price": "0", "customer_id": "17850", "country": "France"},
#     {"invoice_no": "536368", "stock_code": "84029G", "description": "KNITTED UNION FLAG HOT WATER BOTTLE", "quantity": "3", "unit_price": "3.39", "customer_id": None, "country": "Germany"},
#     {"invoice_no": "536369", "stock_code": "22752", "description": "SET 7 BABUSHKA NESTING BOXES", "quantity": "2", "unit_price": "7.65", "customer_id": "13047", "country": "United Kingdom"}
# ]

# print_revenue_report(calculate_total_revenue(orders_raw))