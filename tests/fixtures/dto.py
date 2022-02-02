from dataclasses import dataclass


@dataclass
class Buyer:
    full_name: str
    age: int
    telephone: str


@dataclass
class Order:
    car: str
    vin: int
    price: int
    max_speed: int
    power: int
    buyer: Buyer
