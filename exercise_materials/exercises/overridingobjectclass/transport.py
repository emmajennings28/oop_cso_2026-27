from types import NotImplementedType


class Vehicle:
    def __init__(self,make:str,colour:str,num_seats:int)-> None:
        self.make = make
        self.colour = colour
        self.num_seats = num_seats

    def __str__(self) -> str:
        return f"The make is {self.make}, the colour {self.colour} and number of seats is {self.num_seats}"

    def __repr__(self) -> str:
        return f"Transport [make= {self.make}, colour= {self.colour}, num_seats= {self.num_seats}"

    def __format__(self, format_spec: str) -> str:
        match format_spec.lower():
            case "short":
                return str(self)
            case "long":
                return f"{self.make} {self.colour} with {self.num_seats} seats"
            case "file":
                return f"{self.make}%%{self.colour}%%{self.num_seats}"
            case _:
                return repr(self)

    def __eq__(self, other:object) -> bool | NotImplementedType:
        if not isinstance(other,Vehicle):
            return NotImplemented
        if self.make != other.make:
            return False
        if self.colour != other.colour:
            return False
        if self.num_seats != other.num_seats:
            return False
        return True

    def __ne__(self, other:object) -> bool | NotImplementedType:
        return not self == other

    def __hash__(self) -> int:
        return hash ((self.make,self.colour,self.num_seats))


class Fleet:
    def __init__(self,fleet_name:str):
        self.__fleet_name = fleet_name
        self.__vehicles = []

    def get_vehicles(self)-> list[Vehicle]:
        return list(self.__vehicles)

    def add_vehicle(self, vehicle: Vehicle)->bool:
        if not vehicle:
            return False

        self.__vehicles.append(Vehicle)
        return True

    def remove_vehicle(self,vehicle: Vehicle)->bool:
        if not vehicle:
            return False

        if vehicle in self.__vehicles:
            self.__vehicles.remove(vehicle)
            return True
        return False

    def get_vehicle_count(self)->int:
        return len(self.__vehicles)

    def get_vehicles_by_make(self,make:str)-> list[Vehicle]:
        matches = []
        if not make:
            return matches

        make = make.lower()
        for vehicle in self.__vehicles:
            if vehicle.make.lower()==make:
                matches.append(vehicle)

        return matches

    def __str__(self) -> str:
        return f"{self.__fleet_name} contains {len(self.__vehicles)} vehicles"

    def __repr__(self) -> str:
        return f"Fleet{{fleet_name={self.__fleet_name},vehicles={self.__vehicles}}}"
    def __format__(self, format_spec) -> str:
        if not format_spec:
            return str(self)

        match format_spec.lower():
            case "short":
                return f"{self.__fleet_name}"
            case "long":
                vehicle_text = ""
                for i, vehicle in enumerate(self.__vehicles):
                    vehicle_text += vehicle
                    if i < len(self.__vehicles)-1:
                        vehicle_text += ", "

                return f"{self.__fleet_name}: {vehicle_text}"
            case "file":
                vehicle_text = ""
                for i, vehicle in enumerate(self.__vehicles):
                    vehicle_text += format(vehicle, "file")
                    if i < len(self.__vehicles)-1:
                        vehicle_text += ","
                return f"{self.__fleet_name}##{vehicle_text}"
            case _:
                return str(self)

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other,Fleet):
            return NotImplemented
        if self.__fleet_name.lower() != other.__fleet_name.lower():
            return False
        return True
    def __ne__(self,other: object) -> bool | NotImplementedType:
        return not self == other

    def display_duplicates(self) -> list[Vehicle]:
        duplicates = []

        if not vehicles:
            return duplicates

        for vehicle in self.__vehicles:
            if self.__vehicles.count(vehicle) > 1 and vehicle not in duplicates:
                duplicates.append(vehicle)
        return duplicates

    def find_uniques(self) -> list[Vehicle]:

        uniques = []
        for vehicle in self.__vehicles:
            if self.__vehicles.count(vehicle) == 1:
                uniques.append(vehicle)

        return uniques

    def write_vehicles_to_file(self, filename: str) -> None:
        if not filename:
            return
        with open(filename, "a") as file:
            for vehicle in self.__vehicles:
                file.write(f"{vehicle:file}\n")


