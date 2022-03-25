from dataclasses import dataclass, field
from datetime import date, datetime, time


@dataclass
class Person:
    name: str
    birth_dt: datetime
    date_of_birth: date = field(init=False)
    time_of_birth: time = field(init=False)

    def __post_init__(self):
        self.date_of_birth = self.birth_dt.date()
        self.time_of_birth = self.birth_dt.time()

class Simulator:
    def __init__(self, ips: int) -> None:
        self._iterations_per_second = ips