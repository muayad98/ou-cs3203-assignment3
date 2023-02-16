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

def reverse_list(numbers):
    return numbers[::-1]

def main():
    # Get input from user
    user_input = input("Enter a list of numbers, separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]

    # Call the functions and print the results
    sum_result = sum_list(numbers)
    multiply_result = multiply_list(numbers)
    reverse_result = reverse_list(numbers)
    print("Sum:", sum_result)
    print("Product:", multiply_result)
    print("Reversed List:", reverse_result)

if __name__ == "__main__":
    main()

