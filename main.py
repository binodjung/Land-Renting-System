import operations
import write 
#creating land_dictionary
land_dictionary = {
    '101': ["Kathmandu", "North", 4, 50000, "Not Available"],
    '102': ["Pokhara", "South", 5, 60000, "Available"],
    '103': ["Butwal", "North", 6, 50000, "Available"],
    '104': ["Bhaktapur", "East", 7, 60000, "Available"],
    '105': ["Lalitpur", "West", 3, 20000, "Not Available"]
}

'''initializion of rented_lands and returned_lands lists.'''
rented_lands = []
returned_lands = []

while True:
    print("-"*60)
    print("-"*60)
    print("\n")
    print ("\t\tTechno Property Nepal ")
    print("\t\t Kamalpokhari Kathmandu")
    print("\t\tcontact:9818597973")
    print("\n")
    print("choose the option you want to continue")
    print("-"*60)
    print("press 1. to rent a land")
    print("press 2. to return a land.")
    print("press 3. to exit the system.")
    print("-"*60)
    choice = input("Enter your choice: ")
#Implementation of try and except
    try:
        choice = int(choice)

        if choice == 1:
            while True:
                try:
                    customer_name = input("Enter your name: ")
                    if customer_name.isalpha():
                        break
                    else:
                        print("Error: Please enter alphabetic characters only.")
                except EOFError:
                    print("Error: Input was interrupted. Please provide your name.")

            while True:
                try:
                    address = input("Enter your address: ")
                    if address.isalpha():
                        break
                    else:
                        print("Error: Please enter alphabetic characters only.")
                except EOFError:
                    print("Error: Input was interrupted. Please provide your address.")

            print("\nAvailable Lands:")
            print("--------------------------------------------------------------------")
            print("Kitta No.\tDistrict\tDirection\tAnna\tPrice\tAvailability")
            for key, value in land_dictionary.items():
                if value[4] == "Available":
                    print("{:<10}\t{:<10}\t{:<10}\t{:<5}\t{:<5}\t{:<10}".format(key, value[0], value[1], value[2], value[3], value[4]))
            print("--------------------------------------------------------------------")
            
            kitta_no = input("Enter the id of the land you want to rent: ")
            if kitta_no in land_dictionary:
                selected_land = land_dictionary[kitta_no]
                if selected_land[4] == "Available":
                    
                    while True:
                        try:
                            user_month = int(input("For how many months would you like to rent? Please enter the duration: "))
                            if user_month <= 0:
                                raise ValueError("Invalid input! Please enter a positive integer for the duration.")
                            break
                        except ValueError as ve:
                            print(ve)

                    total = user_month * selected_land[3]
                    rented_lands.append((kitta_no, *selected_land[:4], user_month, total))
                    selected_land[4] = "Not Available"
                    print("Land rented successfully!")
                    operations.generate_rent_invoice(customer_name, address, rented_lands)
                    write.rent_bill(customer_name, address, rented_lands)
                    write.update_status(land_dictionary)
                else:
                    print("The selected land is not available for rent.")
            else:
                print("Invalid kitta number.")

        elif choice == 2:
            while True:
                try:
                    customer_name = input("Enter your name: ")
                    if customer_name.isalpha():
                        break
                    else:
                        print("Error: Please enter alphabetic characters only.")
                except EOFError:
                    print("Error: Input was interrupted. Please provide your name.")

            while True:
                try:
                    address = input("Enter your address: ")
                    if address.isalpha():
                        break
                    else:
                        print("Error: Please enter alphabetic characters only.")
                except EOFError:
                    print("Error: Input was interrupted. Please provide your address.")
            print("\nRented Lands:")
            print("Kitta No.\tDistrict\tDirection\tAnna\tPrice\tAvailability")
            print("--------------------------------------------------------------------")
            for key, value in land_dictionary.items():
                if value[4] == "Not Available":
                    print("{:<10}\t{:<10}\t{:<10}\t{:<5}\t{:<5}\t{:<10}".format(key, value[0], value[1], value[2], value[3], value[4]))
            print("--------------------------------------------------------------------")


            kitta_no = input("Enter the id of the land you want to return: ")
            if kitta_no in land_dictionary:
                selected_land = land_dictionary[kitta_no]
                if selected_land[4] == "Not Available":
                    rent_month = int(input("Enter the month when you rented the land: "))
                    return_month = int(input("Enter the month when you are returning the land: "))
                    if return_month <= rent_month:
                        fine = 0
                    else:
                        fine = (return_month - rent_month) * 0.1 * selected_land[3]
                    total = fine + (return_month * selected_land[3])
                    returned_lands.append((kitta_no, *selected_land[:4], rent_month, return_month, fine, total))
                    selected_land[4] = "Available"
                    print("Land returned successfully!")
                    operations.generate_return_invoice(customer_name, address, returned_lands)
                    write.return_bill(customer_name, address, returned_lands)
                    write.update_status(land_dictionary)
                else:
                    print("The selected land has not been rented.")
            else:
                print("Invalid kitta number.")

        elif choice == 3:
            print("Thank you for using our land rental system.")
            break

        else:
            print("Invalid choice! Please try again.")
    except ValueError:
        print("Invalid input! Please enter a valid integer choice.")

