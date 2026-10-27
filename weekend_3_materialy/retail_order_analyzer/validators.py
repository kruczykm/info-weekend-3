MIN_VALID_QUANTITY = 1
MIN_VALID_PRICE = 0.0

def is_valid_quantity(quantity: int) -> bool:
     return quantity > MIN_VALID_QUANTITY

def is_valid_price(price: float) -> bool:
     return price > MIN_VALID_PRICE

def is_valid_order(order: dict) -> bool:
     quantity = int(order["quantity"])
     price = float(order["unit_price"]) 
     return is_valid_quantity(quantity) and is_valid_price(price)
