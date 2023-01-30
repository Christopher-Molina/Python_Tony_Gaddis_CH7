# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 15
import matplotlib.pyplot as plt


def main():
    # Open file for reading
    infile = open('1994_Weekly_Gas_Averages.txt', 'r')

    # Read file into a list
    averages = infile.readlines()

    # Close the file
    infile.close()

    # Strip the newline character from the file
    for line in range(len(averages)):
        averages[line] = float(averages[line])

    # Create a list with the x and y coordinates of each data point
    x_coords = []
    y_coords = []
    for index in range(len(averages)):
        x_coords.append(index), y_coords.append([averages[index]])

    # Build the line graph
    plt.plot(x_coords, y_coords)

    # Add a title
    plt.title('1994 Weekly Gas Averages')

    # Add labels to the axes
    plt.xlabel('Weeks')
    plt.ylabel('Prices')

    # Add a grid
    plt.grid(True)

    # Display the line graph
    plt.show()


# Call the main function
if __name__ == '__main__':
    main()
