
menu = {
    "Normal Tea": 10,
    "Coffee": 15,
    "Cold Coffee": 20,
    "Hot Milk": 25,
    "Ginger Tea": 50,
    "Green Tea": 100
}

print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")


total = 0
order_details = []

while True:
    tea = input("Which tea do you want? ").title()

    if tea in menu:
        price = menu[tea]
        tax = 0

        # Apply tax
        if tea == "Ginger Tea":
            tax = price * 0.05
        elif tea == "Green Tea":
            tax = price * 0.10

        total += price + tax
        order_details.append((tea, price, tax))
        print(f"Added {tea}. Price: Rs {price: .2f}, Tax: Rs {tax: .2f}")
    else:
        print("Item not available.")

    x = input("Do you want another item? (yes or no) ").strip().lower()
    if x != 'yes':
        break

# Print final bill
print("\nOrder Summary:")
for item, price, tax in order_details:
    print(f"{item}: Rs {price: .2f} + Tax: Rs {tax: .2f}")

if total >= 1000:
    discount = total * 0.10
    final_amt = total - discount
    print(f'final amount after discount is: Rs {final_amt: .2f}')
elif (total > 500) and (total < 1000):
    discount = total * 0.05
    final_amt = total - discount
    print(f'final amount after discount is: Rs {final_amt: .2f}')
else:
    print(f'Total Amount is {total: .2f}')

print("........")