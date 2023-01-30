# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 6
import random


def main():
    try:
        # Get numbers list
        numbers = get_numbers_list()

        # Input n
        n = get_n()

        # Calculate numbers from the list greater than n
        greater_than_n(numbers, n)
    except (TypeError, ValueError, IndexError) as e:
        print(e)


# Function returns a random numbers list in the range of 1, 100
def get_numbers_list():
    scale = int(input('How many random numbers would you like to generate in the list? '))

    while scale < 0:
        scale = int(input('Enter a non-negative numerical value, try again: '))

    numbers = [0] * scale
    for index in range(len(numbers)):
        numbers[index] = random.randint(1, 999)
    return numbers


# Function returns a number
def get_n():
    return int(input('Enter an integer to compare to numbers in the list: '))


# Function calculates numbers that are greater than n in the list
def greater_than_n(numbers, n):
    string = ''
    for index in range(len(numbers)):
        if numbers[index] > n:
            if numbers[index] != numbers[len(numbers) - 1]:
                string += str(numbers[index]) + ', '
            else:
                string += 'and ' + str(numbers[index])

    print('List:', numbers)
    print(f'Numbers greater than {n} in the list are {string}')


# Call the main function
if __name__ == '__main__':
    main()
