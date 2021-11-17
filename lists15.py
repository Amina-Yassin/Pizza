

size = int(input("Which size pizza would you like? type 1 for Small, 2 for Medium, 3 for Large."))


address = input("Please enter your address.")
contact = input ("PLease enter your contactc information")


def toppings():
    orderlist = [""]
    cost = [""]
    toppings_cost1 = 2.00
    toppings1 = ["Done",
    "1. Pepperoni", 
    "2. Mushrooom",
    "3. Extra Cheese",
    "4. Olives", 
    "5. Sausage", 
    "6. Pineapple"]
    choice = 10
    while choice != 0:
        choice = int(input("Please enter which topping you would like. Each  If you are finished adding, type 0."))
        print (toppings1)           
        cost.append(toppings_cost1)
        if choice == 1:
            print (toppings1[choice])
            orderlist.append("Pepperoni")
            toppings_cost1 = toppings_cost1 + 2.00
    print (orderlist)
toppings()