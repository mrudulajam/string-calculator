
import re

def add(numbers: str) -> int:
    return 0

def add(numbers: str) -> int:
    if not numbers:
        return 0
    return int(numbers)

def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, numbers.split(",")))

def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, numbers.split(",")))

def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    return sum(map(int, numbers.split(","))) 
	


def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Check for custom delimiter
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:] 
        numbers = parts[1]  
    else:
        delimiter = ","

    # Replace newlines with the chosen delimiter
    numbers = re.split(f"[{delimiter}\n]", numbers)
    
    return sum(map(int, numbers))
	

def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Check for custom delimiter
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]  # Extract delimiter after "//"
        numbers = parts[1]  
    else:
        delimiter = ","

    # Replace newlines with the chosen delimiter
    numbers = re.split(f"[{delimiter}\n]", numbers)

    # Convert to integers
    num_list = list(map(int, numbers))

    # Find negative numbers
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(num_list)


