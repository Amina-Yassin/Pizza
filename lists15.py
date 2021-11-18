def customization():
    
    cost = 0
    toppings_cost1 = 0
    toppings1 = ["0. Done",
    "1. Pepperoni", 
    "2. Mushrooom",
    "3. Extra Cheese",
    "4. Olives", 
    "5. Sausage", 
    "6. Pineapple"]

    toppings2 = ("""
    0. Done
    1. Pepperoni 
    2. Mushrooom
    3. Extra Cheese
    4. Olives 
    5. Sausage 
    6. Pineapple""")

    toppings3 = (""" 0. Done  1. Pepperoni  2. Mushrooom  
    3. Extra Cheese 4. Olives   5. Sausage 
    6. Pineapple""")


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
        choice = int(input("Please enter which topping you would like.\n {} \n\n Each topping costs $2.00.  If you are finished adding, type 0.".format(toppings2)))
        print (toppings3)           
        if toppings1[choice] == toppings1[1]:
            print ()
            orderlist.append("Pepperoni")
            toppings_cost1 = toppings_cost1 + 2.00
            print ()
            print ("Your total so far is ${}. Plus ${} for the newest topping: {}.".format(cost, toppings_cost1,"Pepperoni"))
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[2]:
            print ()
            orderlist.append("Mushroom")
            toppings_cost1 = toppings_cost1 + 2.00
            print ()
            print ("Your total so far is ${}. Plus ${} for the newest topping: {}.".format(cost, toppings_cost1,"Mushroom"))
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[3]:
            print ()
            orderlist.append("Extra Cheese")
            toppings_cost1 = toppings_cost1 + 2.00
            print ()
            print ("Your total so far is ${}. Plus ${} for the newest topping: {}.".format(cost, toppings_cost1,"Extra Cheese"))
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[4]:
            print ()
            orderlist.append("Olives")
            toppings_cost1 = toppings_cost1 + 2.00
            print ()
            print ("Your total so far is ${}. Plus ${} for the newest topping: {}.".format(cost, toppings_cost1,"Olives"))
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[5]:
            print ()
            orderlist.append("Sausage")
            toppings_cost1 = toppings_cost1 + 2.00
            print ()
            print ("Your total so far is ${}. Plus ${} for the newest topping: {}.".format(cost, toppings_cost1,"Sausage"))
            cost = cost + 2.00
        elif toppings1[choice] == toppings1[6]:
            print ()
            orderlist.append("Pineapple")
            toppings_cost1 = toppings_cost1 + 2.00
            print ()
            print ("Your total so far is ${}. Plus ${} for the newest topping: {}.".format(cost, toppings_cost1,"Pineapple"))
            cost = cost + 2.00
        elif choice > 6:
            print ()
            print ("That is not a valid choice. Try again.")
    print ()
    print ("Your order is: {}".format(orderlist))
    print ("Your total so far is {}$, with {}$ total for the topping(s).".format(cost, toppings_cost1) )
    print ()
    return (orderlist,toppings_cost1,cost)



(order, topcost, total) = customization()
# print (order)

address = input("Please enter your address.")
contact = input ("PLease enter your contact information")

def information (location, coninfo) :
    current = float(input("Please enter the current time to the closest hour. "))
    timetaken = (current + 0.25)
    check = int(input("Is this your correct address? {}. If it is, type 1, if not, type 2.".format(location)))
    if check == 1 or check == "one":
            print ("Your pizza shall be delivered at {}pm/am, please be prepared to pay. You will be notified of your deliver when it arrives at {}.".format(timetaken,location))
    while check != 1:
        # check = input("Is this your correct address? {}. If it is, type 1, if not, type 2.".format(location))
        if check == 2 or check == "two":
            location = input("Please enter your address.")
        else:
            location = input("Please enter your address.")        
      


information(address,contact)