class RzaDevice:
    def __init__(
        self,
        device_id: int | None = None,
        serial_number: str | None = None,
        inventory_number: str | None = None,
    ) -> None:
        self.id = device_id
        self.serial_number = serial_number
        self.inventory_number = inventory_number
