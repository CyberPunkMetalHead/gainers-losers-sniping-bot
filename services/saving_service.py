import json
from pathlib import Path
from typing import List
from models.order import OrderResponse


class SavingService:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def _ensure_file_exists(self):
        if not self.file_path.exists():
            self.file_path.write_text("[]")

    def save_order(self, order: OrderResponse):
        self._ensure_file_exists()
        with self.file_path.open("r+") as file:
            data = json.load(file)
            data.append(order.to_dict())  # Convert OrderResponse to dict and append
            file.seek(0)  # Go to the beginning of the file
            json.dump(data, file, indent=4)

    def load_orders(self) -> List[OrderResponse]:
        self._ensure_file_exists()
        with self.file_path.open("r") as file:
            data = json.load(file)
            return [OrderResponse.from_dict(order) for order in data]

    def delete_order(self, order_id: int):
        self._ensure_file_exists()
        with self.file_path.open("r+") as file:
            data = json.load(file)
            updated_data = [order for order in data if order.get("orderId") != order_id]
            file.seek(0)  # Go to the beginning of the file
            file.truncate()  # Clear existing content
            json.dump(updated_data, file, indent=4)

    def clear_orders(self):
        self.file_path.write_text("[]")  # Reset file with an empty list
