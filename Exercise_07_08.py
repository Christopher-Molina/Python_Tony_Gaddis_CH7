# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 8
NAMES = 200


def main():
    try:
        # Read text files into lists
        girl_names, boy_names = get_names()

        # Input girl name, boy name, or both
        option = get_option()

        # Display results
        results(option, girl_names, boy_names)
    except (IOError, IndexError, TypeError, ValueError) as e:
        print(e)


# Function reads text files into a list
def get_names():
    # Open GirlNames.txt for reading
    infile = open('GirlNames.txt', 'r')

    # Read file into a list
    girl_names = infile.readlines()

    # Open BoyNames.txt for reading
    infile = open('BoyNames.txt', 'r')

    # Read file into a list
    boy_names = infile.readlines()

    # Close the file
    infile.close()

    # Remove newline character from lists
    for index in range(NAMES):
        girl_names[index] = girl_names[index].rstrip('\n')
        boy_names[index] = boy_names[index].rstrip('\n')

    # Return lists
    return girl_names, boy_names


# Function gets an option from the user to enter a girl name, boy name, or both
def get_option():
    # Display header
    print('200 Most Popular Names in the United States (2000-2009:')
    print('1. Search for a girl name.\n2. Search for a boy name.\n3. Search for a girl name and boy name.')
    return int(input('\nEnter your option: '))


# Function displays the results
def results(option, girl_names, boy_names):
    flag = True
    while flag:
        # Check for popularity
        if option == 1:
            print('\nEnter a girl name: ', end='')
            girl_name = get_name()
            print(f'{girl_name}: {is_popular(girl_name, girl_names)}')
            another = get_answer()
            if another:
                option = get_option()
            else:
                flag = False
        elif option == 2:
            print('\nEnter a boy name: ', end='')
            boy_name = get_name()
            print(f'{boy_name}: {is_popular(boy_name, boy_names)}')
            another = get_answer()
            if another:
                option = get_option()
            else:
                flag = False
        elif option == 3:
            print('\nEnter a girl name: ', end='')
            girl_name = get_name()
            print('Enter a boy name: ', end='')
            boy_name = get_name()
            print(f'{girl_name}: {is_popular(girl_name, girl_names)}')
            print(f'{boy_name}: {is_popular(boy_name, boy_names)}')
            another = get_answer()
            if another:
                option = get_option()
            else:
                flag = False
        else:
            print('\nEnter a valid response, re-run the program and try again.')


# Function prompts user to enter a name and returns the name
def get_name():
    name = input()
    while name.isalpha() is False:
        name = input('\nEnter a valid name: ')
    return name


# Function determines name's popularity from 2000-2009
def is_popular(name, name_list):
    popularity = 'Not popular'
    for index in range(len(name_list)):
        if name.lower() == name_list[index].lower():
            popularity = 'Popular'
            break
        else:
            continue
    return popularity


# Function determines if user wants to enter another name
def get_answer():
    answer = input('\nDo you want to enter another another name (y = yes, anything else = no)? ').lower()
    if answer == 'y' or answer == 'yes':
        print()
        return True
    else:
        return False


# Call the main function
if __name__ == '__main__':
    main()
