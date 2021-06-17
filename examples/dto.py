from dataclasses import dataclass, field


@dataclass
class Transport:
    model: str
    speed: int
    gearbox: dict = field(default_factory=lambda x: dict)


class Car(Transport):
    pass


class Moto(Transport):
    pass
