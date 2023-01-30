# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 14
import matplotlib.pyplot as plt


def main():
    # Open file for reading
    infile = open('expenses.txt', 'r')

    # Read file into a list
    expenses = infile.readlines()

    # Close the file
    infile.close()

    # Strip the newline character from the list
    for line in range(len(expenses)):
        expenses[line] = expenses[line].rstrip('\n')

    # Create a list of labels for the slices
    slice_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Miscellaneous']

    # Create a pie chart from the values
    plt.pie(expenses, labels=slice_labels)

    # Add a title
    plt.title('Monthly Expenses')

    # Display the pie chart
    plt.show()


# Call the main function
if __name__ == '__main__':
    main()
