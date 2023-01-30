# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 2
import random
SCALE = 7
MIN = 0
MAX = 10


def main():
    # Generate random 7 integer list
    numbers = get_numbers()

    # Display list
    print(numbers)


# Function generates 7 random integers in a list
def get_numbers():
    numbers = [0] * SCALE
    for index in range(len(numbers)):
        numbers[index] = random.randint(MIN, MAX)

    return numbers


# Call the main function
if __name__ == '__main__':
    main()
