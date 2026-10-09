import random
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ValueInterval:
    """Base interval of values"""

    min_val: float
    max_val: float
    accuracy: int = 100
    step: float = 0.01

    @property
    def value(self) -> float:
        start = int(self.min_val * self.accuracy)
        end = int(self.max_val * self.accuracy)
        step = int(self.step * self.accuracy)
        return random.randrange(start, end, step) / self.accuracy


# Полноценное создание дочерних типов (наследование)
@dataclass(slots=True, frozen=True)
class VoltageInterval(ValueInterval):
    """Interval of voltage values specified in volts"""

    pass


@dataclass(slots=True, frozen=True)
class CurrentInterval(ValueInterval):
    """Interval of current values specified in amperes"""

    pass


@dataclass(slots=True, frozen=True)
class TimeInterval(ValueInterval):
    """Interval of time values specified in seconds"""

    accuracy: int = 1000
    step: float = 0.001
