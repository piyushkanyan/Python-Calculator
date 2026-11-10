product_ids = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12]
prodcut_name = ["rice","milk","bread","eggs","banana","tomato","cooking oil","apple","soap","toothpaste","shampoo","potato"]
product_price = [60 ,30 ,40 ,90 ,50 ,45 ,180 ,120 ,35 ,95 ,180 ,35]
budget = int(input("Enter Your budget: $"))
print("--------------------------------------")
print("        SMART SHOPPING MART           ")
print("--------------------------------------")
options_ids= [1 ,2 ,3 ,4 ,5 ,6 ]
options_name = ["View Products", "Add Product", "Remove Product", "Update Quantity", "View Cart", "Exit"]

for i in range(len(options_ids)):
    print(options_ids[i], options_name[i])
print("--------------------------------------")
Products_cart = []
product_quantity_cart =[]
while True:
    options = int(input("Choose an option: "))
    if options == 6:
        print("Thanks for using this shopping cart program")
        break
    elif options == 1:
        for i in range(len(product_ids)):
            print(product_ids[i],prodcut_name[i],product_price[i])
    elif options == 2:
        while True:
            product = int(input("Enter Prodcut ID to buy (0 to stop or back to menu): "))
            if product == 0:
                break
            else:
                Quantity = int(input("How much quantity want to buy? "))
                if Quantity >0:
                    checking_product_index = product_ids.index(product)
                    name_index = prodcut_name[checking_product_index]
                    print(f"{name_index} Added successfully")
                else:
                    print("The quantity must be greater than zero and cannot be negative")
                Products_cart.append(product)
                product_quantity_cart.append(Quantity)
    elif options == 3:
        remove_product = int(input("Enter the ID number want to remove from the cart:"))
        if remove_product in Products_cart:
            Products_cart.remove(remove_product)
            print("Removed!")
        else:
            print("That ID product is not in your car")
            print(Products_cart)
    elif options == 4:
        update_id = int(input("Enter the ID to update the quantity: "))
        if update_id in Products_cart:
            index = Products_cart.index(update_id)
            updated_quantity = int(input("Enter the new quantity: "))
            if updated_quantity >0:
                product_quantity_cart[index] = updated_quantity
                print("Updated succesfully")
            else:
                Products_cart.pop(index)
                print("Quantity is zero")
        else:
            print("The ID is not in your cart")
    elif options == 5:
        print("-----------------------------")
        print("PRODUCTS IDs, NAME AND PRICE")
        print("-----------------------------")
        for i in range(len(product_ids)):
                    print(product_ids[i],prodcut_name[i],product_price[i])
        print("-------------------------")
        print("       YOUR CART         ")
        print("-------------------------")

        if len(Products_cart) == 0:
            print("The cart is empty")
        else:
            total = 0
            for i in range(len(Products_cart)):
                pos = product_ids.index(Products_cart[i])
                pro_name = prodcut_name[pos]
                price_pos = product_price[pos]
                quan = product_quantity_cart[i]
                price = price_pos * quan
                total += price
                print(f"Product name: {pro_name}, Quantity: {quan}, Price: {price}") 
            print(f"Total Price is: ${total}")

            membership = input("Do you have a membership card? (yes or no): ").strip().lower()
            if membership == "yes":
                print(f"You got 6% Discount, Now Total price becomes only {total * 0.06}")
                if total > budget:
                    print("Warning!!")
                    print(f"Your budget has been exceeded by {total - budget}")
                                
                else:
                    print(f"You bought everything in your budget: Budget was {budget} and total come {total * 0.06}")
                    print("Thanks for purchasing, Enjoy sir/mam !")
            else:
                print(f"If you buy the membership card, you will get 6% Discount on every shopping, now you toal price becomes {total}")
                if total > budget:
                    print("Warning!!")
                    print(f"Your budget has been exceeded by {total - budget}")
                    warn = input("Are you OK! with the toal price? (yes or no)").lower().strip()     
                    if warn =="yes":
                        print("Enjoy")
                    else:
                        print("!! SECUIRTYYY !!")                
                else:
                    print(f"You bought everything in your budget: Budget was {budget} and total come {total}")
                    print("Thanks for purchasing, Enjoy sir/mam !")
    else:
        print("The option doesn't exist in program")        
