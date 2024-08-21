menu = {
    "aloo tikki": 5,
    "maharaja": 10,
    "mac special": 15
}

def take_order():
    print("Menu:")
    print("sr.  name           price")
    for i, item in enumerate(menu.keys(), start=1):
        print(f"{i}.   {item:<15} {menu[item]:>3}$")

    choice = int(input("Enter the number of the item you want to order: "))
    items = list(menu.keys())
    item = items[choice - 1]
    quantity = int(input("Enter the quantity: "))
    is_student = input("Are you a student? (yes/no): ").lower()
    delivery = input("Do you want delivery (yes/no): ").lower()
    tip = 0
    if input("Do you want to give a tip? (yes/no): ").lower() == "yes":
        tip = int(input("Enter the tip amount (2/5/10): "))
    
    total_price = menu[item] * quantity
    discount = 0
    if is_student == "yes":
        discount = total_price * 0.2
    if delivery == "yes":
        total_price *= 1.05
    total_price += tip
    total_price -= discount
    
    print("\n******* Final Bill ********")
    print("sr.  name           price  quantity  total_price")
    print(f"1.   {item:<15} {menu[item]:>3}$   {quantity:<8} {menu[item] * quantity:>5}$")

    print("------------------------------------------")
    print(f"                                {menu[item] * quantity:>5}$")
    if discount:
        print(f"Student discount 20%         -{discount:.2f}$")
    if delivery == "yes":
        print(f"Delivery charge 5%           +{menu[item] * quantity * 0.05:.2f}$")
    if tip:
        print(f"Tip                          +{tip:.2f}$")

    print("---------------------------------------")
    print(f"Total bill                   {total_price:.2f}$")
    print("\nThank you and come again")

take_order()
