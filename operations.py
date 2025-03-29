
def generate_rent_invoice(customer_name, address, rented_lands):
    """It will generate bill after renting land """
    print("\n\t\t\tRent Invoice")
    print("Customer Name:", customer_name)
    print("Address:", address)
    print("\nRent Details:")
    print("--------------------------------------------------------------------------------------")
    print("Kitta No.\tDistrict\tDirection\tAnna\tPrice\tMonths\t\tTotal")
    for land in rented_lands:
        print("{:<10}\t{:<10}\t{:<10}\t{:<5}\t{:<5}\t{:<10}\t{:<1}".format(land[0], land[1], land[2], land[3], land[4], land[5], land[6]))
    print("-------------------------------------------------------------------------------------")
    print("\n\n")

def generate_return_invoice(customer_name, address, returned_lands):
    """It will generate bill after returning land """
    print("\n\t\t\tReturn Invoice")
    print("Customer Name:", customer_name)
    print("Address:", address)
    print("\nReturn Details:")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Kitta No.\tDistrict\tDirection\tAnna\tPrice\tRent Month\tReturn Month\tFine\tTotal")
    for land in returned_lands:
        print("{:<10}\t{:<10}\t{:<10}\t{:<5}\t{:<5}\t{:<10}\t{:<12}\t{:<5}\t{:<5}".format(land[0], land[1], land[2], land[3], land[4], land[5], land[6], land[7], land[8]))
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("\n")


