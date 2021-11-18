

def customization():
    
    cost = 0
    toppings_cost1 = 0
    toppings1 = ["Done",
    "1. Pepperoni", 
    "2. Mushrooom",
    "3. Extra Cheese",
    "4. Olives", 
    "5. Sausage", 
    "6. Pineapple"]
    choice = 10
    size = int(input("Which size pizza would you like? type 1 for Small, 2 for Medium, 3 for Large."))
    if size == 1:
        cost = cost + 12.45
        size = "Small Pizza"
    elif size == 2:
        cost = cost + 18.45
        size = "Medium Pizza"
    elif size == 3:
        cost = cost + 25.00
        size = "Large Pizza"
    
    orderlist = [size]
    
    while choice != 0:
        choice = int(input("Please enter which topping you would like. Each  If you are finished adding, type 0."))
        print (toppings1)           
        if toppings1[choice] == toppings1[1]:
            print (toppings1[choice])
            orderlist.append("Pepperoni")
            toppings_cost1 = toppings_cost1 + 2.00
            print (toppings_cost1)
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[2]:
            print (toppings1[choice])
            orderlist.append("Mushroom")
            toppings_cost1 = toppings_cost1 + 2.00
            print (toppings_cost1)
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[3]:
            print (toppings1[choice])
            orderlist.append("Extra Cheese")
            toppings_cost1 = toppings_cost1 + 2.00
            print (toppings_cost1)
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[4]:
            print (toppings1[choice])
            orderlist.append("Olives")
            toppings_cost1 = toppings_cost1 + 2.00
            print (toppings_cost1)
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[5]:
            print (toppings1[choice])
            orderlist.append("Sausage")
            toppings_cost1 = toppings_cost1 + 2.00
            print (toppings_cost1)
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[6]:
            print (toppings1[choice])
            orderlist.append("Pineapple")
            toppings_cost1 = toppings_cost1 + 2.00
            print (toppings_cost1)
            cost = cost + 2.00
        elif choice > 6:
            print ("That is not a valid choice. Try again.")
    print ( orderlist)
    print ("Your total so far is {}$, with {}$ for the topping(s).".format(cost, toppings_cost1) )
    return (orderlist,toppings_cost1,cost)



(order, topcost, total) = customization()
print (order)

address = input("Please enter your address.")
contact = input ("PLease enter your contact information")
def information (location, coninfo) :
    current = input("Please enter the current time ")


information(address,contact)
