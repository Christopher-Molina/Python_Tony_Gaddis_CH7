# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 5


def main():
    try:
        # Open file for reading
        infile = open('charge_accounts.txt', 'r')

        # Read the contents of a file into a list
        accounts = infile.readlines()

        # Close the file
        infile.close()

        # Prompt user for charge account number
        charge_account = int(input('Enter a charge account number: '))

        # Set valid to false initially
        valid = False
        for index in accounts:
            index = int(index)
            if charge_account == index:
                valid = True  # Set valid to true if account number is found
                break  # Break out of loop
            else:
                continue

        if valid:
            print('Valid')
        else:
            print('Invalid')
    except (IOError, TypeError, ValueError, IndexError) as e:
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
