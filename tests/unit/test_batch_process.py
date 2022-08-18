"""
This test is used to calculate available quanity after allocating the quanity to the batch process.

"""
from datetime import date
from src.allocation.domain.model import Batch, OrderLine

def test_allocating_to_a_batch_reduces_the_available_quanity():
    """
    This test is used to calculate available quanity after allocating the quanity to the batch process.
    """
    batch = Batch("batch-001","SMALL-TABLE",qty=20,eta=date.today())
    line = OrderLine('order-ref','SMALL-TABLE', 2)
    batch.allocate(line)
    assert batch.available_quanity == 18
