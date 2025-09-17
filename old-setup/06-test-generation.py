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

# Prompt: Write unit tests for the function using pytest
