# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division with error handling.
    - Converts inputs to float
    - Handles non-numeric input
    - Handles division by zero
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."