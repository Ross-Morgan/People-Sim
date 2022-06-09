from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from threading import Lock, Thread
from time import time as t_time, sleep


def make_constant(prop: property) -> None:
    print(prop)

    name = prop.fget.__name__

    def const_setter(*_, **__):
        """Constant Property"""
        print(f"{name} is constant")

    object.__setattr__(prop, "fset", const_setter)


@dataclass
class Person:
    name: str
    birth_dt: datetime
    date_of_birth: date = field(init=False)
    time_of_birth: time = field(init=False)

    def __post_init__(self):
        self.date_of_birth = self.birth_dt.date()
        self.time_of_birth = self.birth_dt.time()


class TimeLoop:
    def __init__(self, start_time: datetime, increment: timedelta,
                 stop_time: datetime = None, delay: float = 0.0) -> None:
        self._current_time = start_time

        self._start = start_time
        self._stop = stop_time
        self._increment = increment

        self._lock = Lock()
        self._inc_time = self.inc_time_func(delay)
        self._thread = Thread(target=self._inc_time, name="TimeThread", args=(self,),
                              daemon=True)

    def inc_time_func(self, delay: float):
        def _inc_time(self: TimeLoop):
                while True:
                    with self._lock:
                        print(self._current_time, end="  |  ")
                        self._current_time += self._increment
                        print(self._current_time)
                        sleep(delay)
        return _inc_time

    @property
    def time(self) -> datetime:
        with self._lock:
            return self._current_time

    @property
    def start(self) -> datetime:
        return self._start

    @property
    def stop(self) -> datetime | None:
        return self._stop

    def run(self):
        self._thread.start()


class Simulator:
    def __init__(self, ips: int) -> None:
        self._iterations_per_second = ips

    async def run(self, duration: float = 0):
        """
        @param time (float) - number of seconds to run loop for
                default (0) - runs indefinitely
        """

        duration = duration or True

        while True or t_time() + duration:
            event, args, kwargs = self.get_next_event()
            event(*args, **kwargs)

            sleep(time)

    def get_next_event(self):
        """Get next event to run in the event loop"""


tl = TimeLoop(
    start_time=datetime(2021, 11, 23, 10, 10),
    increment=timedelta(days=1),
    delay=1
)

tl.run()
