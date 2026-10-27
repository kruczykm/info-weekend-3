from pricing import calculate_total_revenue
from reports import print_revenue_report

orders = [
    {"invoice_no": "536365", "quantity": "6", "unit_price": "2.55", "country": "United Kingdom"},
    {"invoice_no": "536366", "quantity": "-1", "unit_price": "3.39", "country": "United Kingdom"},
    {"invoice_no": "536367", "quantity": "8", "unit_price": "0", "country": "France"},
]


def main():
    total_revenue = calculate_total_revenue(orders)
    print_revenue_report(total_revenue)


if __name__ == "__main__":
    main()
