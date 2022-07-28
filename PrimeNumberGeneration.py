# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 12
def main():
    # Input integer greater than
    scale = input_validation()

    # Populate list with range 2 up to numbers
    numbers = list(range(2, scale+1))

    # Calculate prime numbers within list
    prime_numbers(numbers)


# Function displays whether numbers are prime or composite
def prime_numbers(numbers):
    primes = []
    composites = []
    for number in range(2, len(numbers)+1):
        if is_prime(number):
            primes.append(number)
        else:
            composites.append(number)
    print(f'Primes: {primes}\nComposites: {composites}')


# Function calculates whether number is prime or not prime
def is_prime(number):
    for index in range(2, number):  # Skip 1 since any number divided by 1 is itself
        if number % index == 0:
            return False
    else:
        return True


# Function validates input from the user
def input_validation():
    # Input integer greater than 1
    scale = input('Range: ')

    # Input validation
    while scale.isdigit() is False or int(scale) < 2:  # Input must be a digit and greater than 1
        scale = input('Enter a numerical value grater than 1, try again: ')

    # Return string converted to an int
    return int(scale)


# Call the main function
if __name__ == '__main__':
    main()
