import pytest
from setlogging import get_logger

def test_basic_logger():
    logger = get_logger()
    assert logger is not None
