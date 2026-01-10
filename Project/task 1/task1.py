print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")

prices = []
pizza_number = 1

while len(prices) < 4:
    try:
        price = float(input(f"Enter Price of Pizza #{pizza_number}: "))

        if price <= 0:
            print("Please enter a valid price!")
            continue

        prices.append(price)
        pizza_number += 1

    except ValueError:
        print("Please enter a valid price!")

original_total = sum(prices)
cheapest_pizza = min(prices)
final_total = original_total - cheapest_pizza

discount = original_total - final_total
discount_percentage = (discount / original_total) * 100

print(
    f"Order Total is £{final_total:.2f}, "
    f"a fabulous discount of {discount_percentage:.0f}%!"
)
