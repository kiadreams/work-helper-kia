from datetime import datetime


class RzaDevice:
    def __init__(
        self,
        device_id: int | None = None,
        year_of_manufacture: int | None = None,
        month_of_manufacture: int | None = None,
        commissioning_year: int | None = None,
        commissioning_month: int | None = None,
        commissioning_day: int | None = None,
    ) -> None:
        self.id = device_id
        self.year_of_manufacture = year_of_manufacture
        self.month_of_manufacture = month_of_manufacture
        self.commissioning_year = commissioning_year
        self.commissioning_month = commissioning_month
        self.commissioning_day = commissioning_day
