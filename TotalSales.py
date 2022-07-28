# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 1
DAYS = 7


def main():
    # Input sales
    sales = get_sales()

    # Calculate total
    total = get_total(sales)

    # Display total
    display_total(total)


# Function gets input for the sales list
def get_sales():
    sales = [0.0] * DAYS  # Create an empty list

    # For each day of the week, enter a sale
    for index in range(len(sales)):
        print(f'Day {index+1} sales: ', end='')
        sales[index] = input_validation()
    return sales


# Function calculates the total of the list
def get_total(sales):
    # Initialize accumulator variable
    total = 0.0

    # Add to total per each iteration
    for index in range(len(sales)):
        total += sales[index]

    return total


# Function displays the total of sales for the week
def display_total(total):
    print(f'\nTotal sales for the week is ${total:,.2f}')


# Function validates input by the user
def input_validation():
    value = input()

    flag = True
    while flag:
        if str(value).isdigit() and float(value) >= 0:
            flag = False
        else:
            value = input('Value must be a non-negative number, try again: ')

    return float(value)


# Call the main function
if __name__ == '__main__':
    main()
