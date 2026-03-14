def parse_number(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Invalid number input")

def validate_operation(op):
    allowed = ["+", "-", "*", "/"]
    if op not in allowed:
        raise ValueError("Invalid operation")
    return op
def get_number(msg):
    return int(input(msg))
