def add(numbers: str) -> int:
    return 0
    
    num_list = map(int, numbers.split(','))
    return sum(num_list)

# Test cases
print(add(""))
print(add("1"))
print(add("1,5"))