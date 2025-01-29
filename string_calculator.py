
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

