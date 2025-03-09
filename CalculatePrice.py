import datetime
def calculate_price(closing_date, visit_date, original_price ):
    close = datetime.datetime.strptime(closing_date, '%Y-%m-%d')
    visit = datetime.datetime.strptime(visit_date, '%Y-%m-%d')
    delta = datetime.timedelta(days=7)

    # If visit is after closing date, return original price
    if visit > close:
        return original_price

    # Offset to account for first week and initialize price as original price
    price = original_price
    visit += delta
    while visit <= close:
        price -= (price * 0.10)
        visit += delta
        
    return price

print(calculate_price('2025-04-01', '2025-03-03', 100)) # 4 weeks of discounts
# 65.61
print(calculate_price('2025-04-01', '2025-03-15', 50))  # 2 weeks of discounts
# 40.5
print(calculate_price('2025-04-01', '2025-04-15', 75))  # No discount (visit after closing)
# 75
