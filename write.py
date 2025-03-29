import random


def update_status(land_dictionary):
    """ It will update status of land dictionary """
    file = open("data.txt","w")
    for key,value in land_dictionary.items():
        file.write(str(key)+","+str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4]))
        file.write("\n")
    file.close()
    
def rent_bill(customer_name, address, rented_lands):
    """ It will generate rent bill on txt file"""
    random_num = str(random.randint(1000000, 99999999))
    file_name = random_num + "_Rent.txt"
    with open(file_name, "w") as file:
        file.write("\n\t\t\tRent Invoice\n")
        file.write("Customer Name: " + customer_name + "\n")
        file.write("Address: " + address + "\n")
        file.write("\nRent Details:\n")
        file.write("---------------------------------------------------------------------------------\n")
        file.write("Kitta No.\tDistrict\tDirection\tAnna\tPrice\tMonths\t\tTotal\n")
        for land in rented_lands:
            file.write("{:<10}\t{:<10}\t{:<10}\t{:<5}\t{:<5}\t{:<10}\t{:<1}\n".format(land[0], land[1], land[2], land[3], land[4], land[5], land[6]))
        file.write("---------------------------------------------------------------------------------\n")


def return_bill(customer_name, address, returned_lands):
    """ It will generate retrun bill on txt file"""
    random_num = str(random.randint(1000000, 99999999))
    file_name = random_num + "_Return.txt"
    with open(file_name, "w") as file:
        file.write("\n\t\t\tReturn Invoice\n")
        file.write("Customer Name: {}\n".format(customer_name))
        file.write("Address: {}\n".format(address))
        file.write("\nReturn Details:\n")
        file.write("-------------------------------------------------------------------------------------------------------------------------\n")
        file.write("Kitta No.\tDistrict\tDirection\tAnna\tPrice\tRent Month\tReturn Month\tFine\tTotal\n")
        for land in returned_lands:
            file.write("{:<10}\t{:<10}\t{:<10}\t{:<5}\t{:<5}\t{:<10}\t{:<12}\t{:<5}\t{:<5}\n".format(land[0], land[1], land[2], land[3], land[4], land[5], land[6], land[7], land[8]))
        file.write("-------------------------------------------------------------------------------------------------------------------------\n")

