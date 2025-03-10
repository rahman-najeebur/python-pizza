print("Welcome to Python Pizza Deliveries!!!")
currency = "$"
bill = 0

# display menu
def display_menu():
    print(10*"#" + " Python Pizza Menu " + 2 * "#")
    print(f"Small pizza (S): {currency}10")
    print(f"Medium pizza (M):{currency}15")
    print(f"Large pizza (L): {currency}20")
    print(30*"#")

# extra filling
def extra_filling(size):
    amount = 0
    add_pepperoni = input("Do you want pepperoni? Type Y if yes, N if no: ").lower()
    if add_pepperoni == "y" and size == "s":
        amount = 2
    if add_pepperoni == "y" and (size == "m" or size == "l"):
        amount = 3
    extra_cheese = input("Do you want extra cheese? Type Y if yes, N if no: ").lower()
    if extra_cheese == "y":
        amount += 1
    return amount

# calling the display_menu() function
display_menu()

pizza_choice = input("What pizza Size do you want(S, M, L)?: ").lower()
if pizza_choice == "s":
    bill = 10
    bill += extra_filling(pizza_choice)
elif pizza_choice == "m":
    bill = 15
    bill += extra_filling(pizza_choice)
elif pizza_choice == "l":
    bill = 20
    bill += extra_filling(pizza_choice)
else:
    print("Please select S for Small, M for Medium and L for Large Pizza.")

print(f"Your Total bill is {currency}{bill}")

