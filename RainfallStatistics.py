# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 3
MONTHS = 12


def main():
    # Input rainfall for each month
    rainfall = get_rainfall()

    # Calculate total rainfall
    total_rainfall = get_total_rainfall(rainfall)

    # Calculate average monthly rainfall
    avg_rainfall = get_avg_rainfall(total_rainfall)

    # Calculate maximum and minimum rainfall
    maximum, minimum = get_max_and_min(rainfall)

    # Display results
    display_results(total_rainfall, avg_rainfall, maximum, minimum)


# Function gets the rainfall in inches per month and returns as a list
def get_rainfall():
    # Create twelve element list
    rainfall = [0] * MONTHS

    # For each month, input rainfall amount
    for index in range(len(rainfall)):
        print(f'Total Rainfall Month {index + 1}: ', end='')
        rainfall[index] = input_validation()
    return rainfall


# Function returns the total rainfall per year
def get_total_rainfall(rainfall):
    # Initialize accumulator
    total = 0.0

    for month in range(len(rainfall)):
        total += rainfall[month]

    return total


# Function returns the average rainfall per year
def get_avg_rainfall(total_rainfall):
    return total_rainfall / MONTHS


# Function gets the max rainfall and min rainfall per year
def get_max_and_min(rainfall):
    return max(rainfall), min(rainfall)


# Function displays the results formatted
def display_results(total_rainfall, avg_rainfall, maximum, minimum):
    print(f'\nTotal Rainfall: {total_rainfall:,.2f}')
    print(f'Average Rainfall: {avg_rainfall:,.2f}')
    print(f'Maximum: {maximum:,.2f}')
    print(f'Minimum: {minimum:,.2f}')


# Function validtaes input from the user
def input_validation():
    value = input()
    flag = True

    while flag:
        if str(value).isdigit() and float(value) >= 0:
            flag = False
        else:
            value = input('Enter a non-negative numerical value, try again: ')
    return float(value)


# Call the main function
if __name__ == '__main__':
    main()
