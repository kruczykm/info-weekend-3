from validators import is_valid_order

def calculate_line_total(quantity: int, unit_price: float) -> float:
    return quantity * unit_price

def calculate_total_revenue(orders: list) -> float:
    total_revenue = 0.0

    for order in orders:
        if is_valid_order(order):
            quantity = int(order["quantity"])
            price = float(order["unit_price"])
            total_revenue += calculate_line_total(quantity, price)

    return total_revenue
