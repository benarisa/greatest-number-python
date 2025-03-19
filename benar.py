def get_largest_and_smallest(numbers):
    if len(numbers) == 0:
        return "The list is empty."

    # Assume the first number is both largest and smallest
    largest = smallest = numbers[0]

    # Compare each number to find the largest and smallest
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example of running the program with a new number list
numbers_list = [10, -20, 7, 50, -3, 25]
largest, smallest = get_largest_and_smallest(numbers_list)

print("Largest number:", largest)
print("Smallest number:", smallest)
