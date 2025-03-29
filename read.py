
def read_land():
    """It will read details from data.txt """
    myDictionary = {}
    with open("data.txt", "r") as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip().split(', ')
            kitta = int(line[0])
            district = line[1]
            direction = line[2]
            anna = int(line[3])
            price = int(line[4])
            availability = line[5]
            myDictionary[kitta] = [district, direction, anna, price, availability]
    return myDictionary
