"""
This test is used for calculating available quanity after allocating the quanity to the batch process.

"""
from datetime import date
from src.allocation.domain.model import Batch, OrderLine
import pytest

def test_allocating_to_a_batch_reduces_the_available_quanity():
    """
    This test is used to calculate available quanity after allocating the quanity to the batch process.
    """
    batch = Batch("batch-001","SMALL-TABLE",qty=20,eta=date.today())
    line = OrderLine('order-ref','SMALL-TABLE', 2)
    batch.allocate(line)
    assert batch.available_quanity == 18

def test_to_check_if_allocating_more_than_the_available_quanity_raises_an_error():
    """
    This test is used to check if allocating more than the available quanity raises an error.
    """
    batch = Batch("batch-001","SMALL-TABLE",qty=20,eta=date.today())
    line = OrderLine('order-ref','SMALL-TABLE', 22)
    with pytest.raises(ValueError):
        batch.allocate(line)

def test_to_check_if_allocating_to_a_batch_with_different_sku_raises_an_error():
    """
    This test is used to check if allocating to a batch with different sku raises an error.
    """
    batch = Batch("batch-001","SMALL-TABLE",qty=20,eta=date.today())
    line = OrderLine('order-ref','SMALL-TABLE-2', 2)
    with pytest.raises(ValueError):
        batch.allocate(line)
