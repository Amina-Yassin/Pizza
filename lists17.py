def customization(size):
    
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

    return (orderlist,toppings_cost1, cost)




def information (location) :
    current = float(input("Please enter the current time to the closest hour. Example: 4:45 -> 5. "))
    print ()
    timetaken = (current + 0.25)
    check = int(input("Is this your correct address? {}. If it is, type 1, if not, type 2. ".format(location)))
    while check != 1:
        if check == 2 or check == "two":
            location = input("Please enter your address. ")
            break
        else:
            location = input("Please enter your address. ")
            break        
    return(timetaken,location)
      

def main ():
    print ()
    print("Thank you for ordering from Python Pizza, where the food slithers down your digestive system. ")
    toppings2 = ("""
    0. Done
    1. Pepperoni 
    2. Mushrooom
    3. Extra Cheese
    4. Olives 
    5. Sausage 
    6. Pineapple""")
    size1 = int(input("Which size pizza would you like? type 1 for Small, 2 for Medium, 3 for Large. "))
    print()
    (order,topcost,total) = customization(size1)     
    print ()
    address = input("Please enter your address. ")
    print ()    
    contact = input ("Please enter your contact information. ")      
    print ()
    (deliverytime,address) = information(address)

    print ()
    print ("Your order is: one {}, with {} as toppings.".format(order[0], order[1:]))
    # print ()    
    print ("Your total so far is {}$, with {}$ total for the topping(s).".format(total, topcost) )
    print ()
    print ("Your pizza shall be delivered at {}am/pm, please be prepared to pay. You will be notified when it arrives at {}.".format(deliverytime,address))
    #print ()    
    print ("You shall be contacted at {} when the order arrives.".format(contact))
    print()
    print ("Thank you for your buisness at Python Pizza.")
    print()
#CALL MAIN FUCNTION HERE
if __name__ == "__main__":
    main()
