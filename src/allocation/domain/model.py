from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass(frozen=True)
class OrderLine:
    order_ref: str
    sku: str
    qty: int

    def __post_init__(self):
        if self.qty < 1:
            raise ValueError("Quantity must be greater than 0")

class Batch:
    def __init__(self, batch_id, sku, qty, eta:Optional[date]): # Optional is used to avoid error when eta is not provided
        self.batch_id = batch_id
        self.sku = sku
        self.available_quanity = qty
        self.eta = eta

    def allocate(self, order_line):
        if order_line.sku != self.sku:
            raise ValueError("Cannot allocate order line to a batch with different SKU")
        if order_line.qty > self.available_quanity:
            raise ValueError("Cannot allocate more than the available quanity")
        self.available_quanity -= order_line.qty
        return self.available_quanity