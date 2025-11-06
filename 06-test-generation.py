# The code is a simple function that calculates 
# the unit price of an item given its total price and quantity.

def calculate_unit_price(total_price, quantity):
    """
    Calculate the unit price given the total price and quantity.

    Parameters:
    total_price (float): The total price of the items.
    quantity (int): The number of items.

    Returns:
    float: The unit price of a single item.
    """
    if quantity == 0:
        raise ValueError("Quantity cannot be zero.")
    return total_price / quantity

import pytest

def test_calculate_unit_price_normal():
    """Test normal case with valid inputs."""
    assert calculate_unit_price(100.0, 4) == 25.0

def test_calculate_unit_price_float_quantity():
    """Test with float total_price and integer quantity."""
    assert calculate_unit_price(99.99, 3) == pytest.approx(33.33, rel=1e-2)

def test_calculate_unit_price_single_item():
    """Test with quantity of 1."""
    assert calculate_unit_price(42.0, 1) == 42.0

def test_calculate_unit_price_zero_quantity():
    """Test that zero quantity raises ValueError."""
    with pytest.raises(ValueError, match="Quantity cannot be zero."):
        calculate_unit_price(100.0, 0)

def test_calculate_unit_price_negative_quantity():
    """Test with negative quantity (should return negative unit price)."""
    assert calculate_unit_price(100.0, -4) == -25.0

def test_calculate_unit_price_negative_price():
    """Test with negative total price."""
    assert calculate_unit_price(-100.0, 4) == -25.0

def test_calculate_unit_price_large_values():
    """Test with large values for total_price and quantity."""
    assert calculate_unit_price(1e6, 1000) == 1000.0
