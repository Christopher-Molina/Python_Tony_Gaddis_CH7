# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 7
def main():
    # Answer key for driver's license exam
    answer_key = ['A', 'C', 'A', 'A', 'D',
                  'B', 'C', 'A', 'C', 'B',
                  'A', 'D', 'C', 'A', 'D',
                  'C', 'B', 'B', 'D', 'A']

    # Open file for reading
    infile = open('answers.txt', 'r')

    # Read the contents of a file into a list
    answers = infile.readlines()

    # Close the file
    infile.close()

    # Validate the answers
    correct, incorrect, incorrect_questions = validate(answers, answer_key)

    # Display results
    results(correct, incorrect, incorrect_questions)


# Function returns correct and incorrect answers
def validate(answers, answer_key):
    correct = incorrect = 0
    incorrect_questions = []
    for index in range(len(answers)):
        if answers[index].rstrip('\n') == answer_key[index]:
            correct += 1
        else:
            incorrect += 1
            incorrect_questions.append(index+1)
    return correct, incorrect, incorrect_questions


# Function displays the results
def results(correct, incorrect, incorrect_questions):
    if correct >= 15:
        print('Passed.')
    else:
        print('Failed.')

    print(f'Correct: {correct}')
    print(f'Incorrect: {incorrect}')

    if incorrect >= 1:
        print('Incorrect Questions:', incorrect_questions)


# Call the main function
if __name__ == '__main__':
    main()
