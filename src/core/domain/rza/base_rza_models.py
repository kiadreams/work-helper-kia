from src.core.domain.rza.enums import DeviceStatus


class RzaDevice:
    def __init__(
        self,
        device_id: int | None = None,
    ) -> None:
        self.id = device_id
        self.year_of_manufacture: int | None = None
        self.month_of_manufacture: int | None = None
        self.commissioning_year: int | None = None
        self.commissioning_month: int | None = None
        self.commissioning_day: int | None = None
        self.device_status = DeviceStatus.OPERATION
