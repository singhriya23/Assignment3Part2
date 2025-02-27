import sys
import re

# Define the congestion change consistency function
def congestion_change_consistency(change_in_congestion: str) -> float:
    """
    Converts the change in congestion value to a float.
    If the value is positive, it returns a negative impact (congestion increased).
    If the value is negative, it returns a positive impact (congestion decreased).
    """
    if change_in_congestion:
        change = re.findall(r"[-+]?\d+", change_in_congestion)
        if change:
            value = int(change[0])
            return float(-value)  # Negative means congestion decreased, positive means increased
    return 0.0  # Default to no change

# For local debugging
if __name__ == '__main__':
    # Check if an argument is passed
    if len(sys.argv) > 1:
        # Pass the first argument to the function
        input_value = sys.argv[1]
        result = congestion_change_consistency(input_value)
        print(f"Input: {input_value} -> Output: {result}")
    else:
        print("Please provide an input value. Example: python function.py '1'")
