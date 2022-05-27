from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from threading import Thread, Lock


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
        self._inc_time = self.inc_time_func()
        self._thread = Thread(target=self._inc_time, name="TimeThread",
                              daemon=True)

    def inc_time_func(self):
        def _inc_time(self: TimeLoop):
                while True:
                    with self._lock:
                        self._current_time += self._increment
        return _inc_time

    @property
    def time(self) -> datetime:
        pass
    @property
    def start(self):
        return self._start
    @property
    def stop(self):
        return self._stop

    @time.setter
    def time(self):
        """Keep property constant"""
    @start.setter
    def start(self):
        """Keep property constant"""
    @stop.setter
    def stop(self):
        """Keep property constant"""

    def run(self):
        self._thread.start()


class Simulator:
    def __init__(self, ips: int) -> None:
        self._iterations_per_second = ips

    async def run(self, time: float = 0):
        """
        @param time (float) - number of seconds to run loop for
                default (0) - runs indefinitely 
        """
        while True:
            event, args, kwargs = self.get_next_event()
            event(*args, **kwargs)

    def get_next_event(self):
        pass
