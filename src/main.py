from datetime import datetime


class Person:
    def __init__(self, name: str, birth_dt: datetime) -> None:
        self._name = name
        self._date_of_birth = birth_dt.date()
        self._time_of_birth = birth_dt.time()
        self._birth_dt = birth_dt


class Simulator:
    def __init__(self, ips: int) -> None:
        self._iterations_per_second = ips