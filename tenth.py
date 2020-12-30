class Car(object):

    def __init__(self, number_of_seats, horsepower, color):
        self.number_of_seats = number_of_seats
        self.horsepower = horsepower
        self.color = color
        self.is_engine_started = False

    def turn_on(self):
        self.is_engine_started = True
        print("Engine started...")

    def turn_off(self):
        self.is_engine_started = False
        print("Engine stopped...")

    def accelerate(self):
        if self.is_engine_started:
            print("accelerating...")
        else:
            raise UserWarning("You need to start the car first")

    def sound_horn(self):
        print("regular sound...regular sound")

    def show_details(self):
        print("")
        print(self.__class__)
        print(vars(self))


class StandardCar(Car):

    def __init__(self, number_of_seats=4, horsepower=120, color="white", is_electric=False):
        super().__init__(number_of_seats=number_of_seats, horsepower=horsepower, color=color)
        self.is_electric = is_electric

    def sound_horn(self):
        print("ban ban")


class RaceCar(Car):

    def __init__(self, horsepower=600, color="white"):
        super().__init__(number_of_seats=1, horsepower=horsepower, color=color)
        self.has_nitro = True

    def accelerate(self):
        super().accelerate()
        print("but faster than a normal car")

    def sound_horn(self):
        pass


class Truck(Car):
    def __init__(self, horsepower=400, color="white"):
        super().__init__(number_of_seats=2, horsepower=horsepower, color=color)
        self.has_reserve_tank = True

    def sound_horn(self):
        print("baaaaaannnn...baaaaaannnn")


class RegularTruck(Truck):
    def __init__(self, horsepower=400, color="Silver"):
        super().__init__(horsepower=horsepower, color=color)
        self.engine_type = "gasoline"


class LargeTruck(Truck):
    def __init__(self, horsepower=400, color="Black"):
        super().__init__(horsepower=horsepower, color=color)
        self.engine_type = "diesel"
