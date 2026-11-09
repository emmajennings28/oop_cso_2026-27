from transport import Vehicle


def create_fleet() -> list[Vehicle]:

    vehicle1 = Vehicle("Honda", "Grey", 5)
    vehicle2 = Vehicle("BYD", "Blue", 5)
    vehicle3 = Vehicle("Ford", "Grey", 3)
    vehicle4 = Vehicle("Toyota", "Black", 5)
    vehicle5 = Vehicle("Volkswagen", "Red", 7)
    vehicle6 = Vehicle("Opal", "White", 7)
    vehicle7 = Vehicle("Toyota", "Blue", 4)
    vehicle8 = Vehicle("Cupra", "Black", 6)
    vehicle9 = Vehicle("BYD", "Blue", 5)
    vehicle10 = Vehicle("Volkswagen", "Red", 7)
    vehicle11 = Vehicle("Ford", "Grey", 3)
    return [vehicle1, vehicle2, vehicle3, vehicle4, vehicle5, vehicle6, vehicle7, vehicle8, vehicle9, vehicle10, vehicle11]

def display_all(vehicles: list[Vehicle] )-> None:
    for vehicle in vehicles:
        print(vehicle)

def display_specific(vehicles: list[Vehicle])-> list[Vehicle]:
    number = int(input("Enter a vehicle number 1-11:"))

    if 1 <= number <= len(vehicles):
        print(vehicles[number - 1])
    else:
        print("invalid")

def display_duplicates(vehicles: list[Vehicle])-> list[Vehicle]:
    duplicates = []

    if not vehicles:
        return duplicates

    for vehicle in vehicles:
       if vehicles.count(vehicle) > 1 and vehicle not in duplicates:
           duplicates.append(vehicle)
    return duplicates


def find_uniques(vehicles: list[Vehicle])-> list[Vehicle]:

    uniques = []
    if not vehicles:
        return uniques

    for vehicle in vehicles:
        if vehicles.count(vehicle) ==1:
            uniques.append(vehicle)

    return uniques

def write_vehicles_to_file(vehicle_list: list[Vehicle], filename: str) -> None:
    if not filename:
        return
    with open(filename, "a") as file:
       for vehicle in vehicles:
           file.write(f"{vehicle:file}\n")

if __name__ == "__main__":
    vehicles = create_fleet()

    print("Fleet details:")
    display_all(vehicles)
    print("-"*20)

    print("Specific car details:")
    display_specific(vehicles)
    print("-"*20)

    duplicates = display_duplicates(vehicles)
    print("Duplicate vehicles:")
    display_all(duplicates)
    print("-"*20)

    uniques = find_uniques(vehicles)
    print("Unique vehicles:")
    display_all(uniques)
    print("-"*20)

    write_vehicles_to_file(vehicles, "fleet_details.txt")