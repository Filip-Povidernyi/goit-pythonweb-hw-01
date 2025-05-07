import logging
from abc import ABC, abstractmethod
from typing import Protocol


logging.INFO
logger = logging.getLogger("vehicle_info")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(Protocol):
    @abstractmethod
    def create_car() -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle() -> Vehicle:
        pass


class Car(Vehicle):

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US specs")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US specs")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU specs")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU specs")


def main() -> None:
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    eu_car = eu_factory.create_car("BMW", "X5")

    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Street 750")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Monster 821")

    vehicles = [us_car, eu_car, us_motorcycle, eu_motorcycle]

    for vehicle in vehicles:
        vehicle.start_engine()


if __name__ == "__main__":
    main()
