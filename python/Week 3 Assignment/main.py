def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount_percent >= 20, apply discount.
    Otherwise, return original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(price, discount_percent)


if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
