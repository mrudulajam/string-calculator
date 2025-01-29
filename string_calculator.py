def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    num_list = map(int, numbers.split(','))
    return sum(num_list)

# Test cases
print(add(""))      # Output: 0
print(add("1"))     # Output: 1
print(add("1,5"))   # Output: 6
