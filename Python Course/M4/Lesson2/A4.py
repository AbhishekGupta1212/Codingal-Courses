# Write a Python program to calculate the product, multiplying all the numbers of the given tuple.

def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage:
numbers_tuple = (1, 2, 3, 4, 5)
result = calculate_product(numbers_tuple)
print("The product of the numbers in the tuple is:", result)