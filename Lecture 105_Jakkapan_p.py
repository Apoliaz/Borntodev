class Vehical:
    licenseNumber = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Pickup(Vehical):
    pass
class Car(Vehical):
    pass
class Van(Vehical):
    pass
class Estatecar(Vehical):
    pass

picup1 = Pickup()
picup1.turnOnAirConditioner()
car1 = Car()
car1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()