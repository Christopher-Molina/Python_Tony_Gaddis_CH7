# Starting Out With Pyth 5th Edition: Chapter 8 - Exercise 10


def main():
    try:
        world_series_winners = get_file()

        # Display world series winners
        display_winners(world_series_winners)

        # Input team name
        team = input('\nEnter a team name: ')

        # Check if team is found in list, if not prompt user to try again
        while team not in world_series_winners:
            team = input('Enter a valid team name, try again: ')

        # Calculate numbers of wins
        wins = get_wins(team, world_series_winners)

        # Display wins
        print(f'{team} wins: {wins}')
    except (IOError, ValueError, IndexError, TypeError) as e:
        print(e)


# Function displays world series winners
def display_winners(world_series_winners):
    # Initialize a null list
    unique = []

    # Traverse for all elements
    for index in world_series_winners:
        if index not in unique:
            unique.append(index)

    print('World Series Champions 1903-2009 (World Series not Played in 1904 or 1994):')
    for index in range(len(unique)):
        print(unique[index])


# Function returns a text file
def get_file():
    # Open file
    infile = open('WorldSeriesWinners.txt', 'r')

    # Read files into a list
    world_series_winners = infile.readlines()

    # Strip the newline character from list
    for index in range(len(world_series_winners)):
        world_series_winners[index] = world_series_winners[index].rstrip('\n')

    # Close the file
    infile.close()

    # Return list
    return world_series_winners


# Function returns the number of wins for a specified team
def get_wins(team, world_series_winners):
    # Initialize accumulator variable
    wins = 0

    # For each time team is found, increment wins
    for index in range(len(world_series_winners)):
        if team.lower() == world_series_winners[index].lower():
            wins += 1
    return wins


# Call the main function
if __name__ == '__main__':
    main()
