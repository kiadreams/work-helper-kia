import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from src.core.domain.rza.enums import ValueQuality


@dataclass(slots=True, frozen=True, eq=False)
class MeasuredValue:
    value: float
    creation_time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    quality: ValueQuality = ValueQuality.DEFAULT

    REL_TOL: float = 1e-4
    ABS_TOL: float = 5e-4

    def _merge_quality(self, other: Any) -> ValueQuality:
        """
        Логика 'худшего качества': если хотя бы одно значение не REAL,
        то результат DEFAULT (или SETPOINT, если оба значения - уставки).
        """
        if isinstance(other, MeasuredValue):
            if self.quality == ValueQuality.REAL and other.quality == ValueQuality.REAL:
                return ValueQuality.REAL
            elif self.quality == ValueQuality.SETPOINT or other.quality == ValueQuality.SETPOINT:
                raise ValueError("В расчетах применяется значение уставки вместо измеренного!")
            else:
                return ValueQuality.DEFAULT
        return self.quality

    def _merge_time(self, other: Any) -> datetime:
        """Берет метку времени самого свежего измерения."""
        if isinstance(other, MeasuredValue):
            return max(self.creation_time, other.creation_time)
        return self.creation_time

    def __add__(self, other: MeasuredValue | float | int) -> MeasuredValue:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return MeasuredValue(
                value=self.value + other_value,
                creation_time=self._merge_time(other),
                quality=self._merge_quality(other),
            )
        return NotImplemented

    def __radd__(self, other: MeasuredValue | float | int) -> MeasuredValue:
        return self.__add__(other)

    def __sub__(self, other: MeasuredValue | float | int) -> MeasuredValue:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return MeasuredValue(
                value=self.value - other_value,
                creation_time=self._merge_time(other),
                quality=self._merge_quality(other),
            )
        return NotImplemented

    def __rsub__(self, other: float | int) -> MeasuredValue:
        if isinstance(other, (int, float)):
            return MeasuredValue(other - self.value, self.creation_time, self.quality)
        return NotImplemented

    def __mul__(self, other: MeasuredValue | float | int) -> MeasuredValue:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return MeasuredValue(
                value=self.value * other_value,
                creation_time=self._merge_time(other),
                quality=self._merge_quality(other),
            )
        return NotImplemented

    def __rmul__(self, other: float | int) -> MeasuredValue:
        return self.__mul__(other)

    def __truediv__(self, other: MeasuredValue | float | int) -> MeasuredValue:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            if math.isclose(other_value, 0.0, abs_tol=self.ABS_TOL):
                raise ZeroDivisionError("Деление MeasuredValue на нулевое значение")
            return MeasuredValue(
                self.value / other_value,
                creation_time=self._merge_time(other),
                quality=self._merge_quality(other),
            )
        return NotImplemented

    def __rtruediv__(self, other: float | int) -> MeasuredValue:
        if isinstance(other, (int, float)):
            if math.isclose(self.value, 0.0, abs_tol=self.ABS_TOL):
                raise ZeroDivisionError("Деление числа на нулевое MeasuredValue")
            return MeasuredValue(other / self.value, self.creation_time, self.quality)
        return NotImplemented

    def __eq__(self, other: Any) -> bool:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return math.isclose(self.value, other_value, rel_tol=self.REL_TOL, abs_tol=self.ABS_TOL)
        return False

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: MeasuredValue | float | int) -> bool:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return self.value < other_value and not (
                math.isclose(self.value, other_value, rel_tol=self.REL_TOL, abs_tol=self.ABS_TOL)
            )
        return NotImplemented

    def __le__(self, other: MeasuredValue | float | int) -> bool:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return self.value < other_value or (
                math.isclose(self.value, other_value, rel_tol=self.REL_TOL, abs_tol=self.ABS_TOL)
            )
        return NotImplemented

    def __gt__(self, other: MeasuredValue | float | int) -> bool:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return self.value > other_value and not (
                math.isclose(self.value, other_value, rel_tol=self.REL_TOL, abs_tol=self.ABS_TOL)
            )
        return NotImplemented

    def __ge__(self, other: MeasuredValue | float | int) -> bool:
        other_value = other.value if isinstance(other, MeasuredValue) else other
        if isinstance(other_value, (float, int)):
            return self.value > other_value or (
                math.isclose(self.value, other_value, rel_tol=self.REL_TOL, abs_tol=self.ABS_TOL)
            )
        return NotImplemented
