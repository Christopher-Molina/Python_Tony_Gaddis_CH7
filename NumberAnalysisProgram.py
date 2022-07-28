# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 4
MAX = 20  # Constant for max numbers in list


def main():
    try:
        # Get numbers list
        numbers = get_numbers()

        # Get the lowest number in the list
        lowest = get_lowest(numbers)

        # Get the maximum number in the list
        maximum = get_maximum(numbers)

        # Get the total of the numbers in the list
        total = get_total(numbers)

        # Get the average of the numbers in the list
        average = get_average(numbers)

        # Display the results
        display_results(lowest, maximum, total, average)
    except (TypeError, IndexError, ValueError) as e:
        print(e)


# Function returns a list of numbers
def get_numbers():
    # Prompt user for a series of 20 numbers and store in a list
    numbers = []
    print('Enter a series of 20 numbers')
    [numbers.append(input_validation(index)) for index in range(1, MAX+1)]

    # Return the list
    return numbers


# Function returns the lowest number in the list
def get_lowest(numbers):
    lowest = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] < lowest:
            lowest = numbers[index]
    return lowest


# Function returns the maximum number in the list
def get_maximum(numbers):
    maximum = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] > maximum:
            maximum = numbers[index]
    return maximum


# Function returns total of all numbers in the list
def get_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# Function returns the average of the numbers in the list
def get_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


# Function displays the results
def display_results(lowest, maximum, total, average):
    print(f'\nMin: {lowest}\nMax: {maximum}\nTotal: {total}\nAverage: {average:.2f}')


# Function validates input from the user
def input_validation(index):
    # Prompt user for an integer
    number = input(f'Enter number {index}: ')

    # Validate the input
    while str(number).isdigit() is False:
        number = input(f'ERROR: Enter a valid number, try again: ')

    # Return the number
    return float(number)


# Call the main function
if __name__ == '__main__':
    main()
