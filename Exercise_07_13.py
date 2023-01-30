# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 13
import random


def main():
    # Copy file into a list
    responses = get_file()

    # Prompt user for a question
    magic_8_ball(responses)


# Function returns a text file
def get_file():
    # Open file for reading
    infile = open('8_ball_responses.txt', 'r')

    # Read file into a list
    responses = infile.readlines()

    # Close the file
    infile.close()

    # Strip the newline character from the list
    for line in range(len(responses)):
        responses[line] = responses[line].rstrip('\n')
    return responses


# Function displays a magic 8 ball response until the user quits
def magic_8_ball(responses):
    print('Magic 8 Ball Knows the Answer to Your Questions!')

    # Create a variable to control the loop
    reply = 'Y'
    while reply == 'Y' or reply == 'YES':
        print('Enter a Yes/No Question: ', end='')
        input()
        print(random.choice(responses))
        reply = input('Do you want to ask another question (y = yes, anything else = no)? ').upper()
        print()


# Call the main function
if __name__ == '__main__':
    main()
