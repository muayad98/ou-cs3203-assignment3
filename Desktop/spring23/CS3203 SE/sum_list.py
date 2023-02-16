def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
sum_result = sum_list(numbers)
multiply_result = multiply_list(numbers)
print("Sum:", sum_result)  # Output: 15
print("Product:", multiply_result)  # Output: 120
