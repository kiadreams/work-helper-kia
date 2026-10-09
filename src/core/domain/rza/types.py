from dataclasses import dataclass
import random


@dataclass(slots=True, frozen=True)
class ValueInterval:
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
    """Интервал напряжения"""
    pass


@dataclass(slots=True, frozen=True)
class CurrentInterval(ValueInterval):
    """Интервал тока"""
    pass


@dataclass(slots=True, frozen=True)
class TimeInterval(ValueInterval):
    """Интервал тока"""
    pass
