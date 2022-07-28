# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 9
START_YEAR = 1950


def main():
    try:
        # Open the file
        infile = open('USPopulation.txt', 'r')

        # Read file contents into a list
        population = infile.readlines()

        for index in range(len(population)):
            population[index] = int(population[index])

        # Close the file
        infile.close()

        # Calculate average population during time period
        average = get_average(population)

        # Calculate the year with the greatest increase during time period
        greatest = get_greatest(population)

        # Calculate the year with the smallest increase during time period
        smallest = get_smallest(population)

        # Display results
        results(average, greatest, smallest)
    except IOError:
        print(IOError)
    except IndexError:
        print(IndexError)
    except TypeError:
        print(TypeError)
    except ValueError:
        print(ValueError)


# Function calculates the population average annual change
def get_average(population):
    # Initialize accumulator variable
    change = 0.0

    # For each year, add population increase to total
    for year in range(len(population) - 1, 1, -1):
        change += (population[year]) - (population[year-1])

    # Return average annual change
    return change / len(population)


# Function returns the year with the highest increase
def get_greatest(population):
    highest = population[1] - population[0]
    year = 1
    for index in range(len(population) - 1, 2, -1):
        if population[index] - population[index-1] > highest:
            highest = population[index] - population[index-1]
            year = index

    return START_YEAR + year


# Function returns the year with the smallest increase during time period
def get_smallest(population):
    smallest = population[1] - population[0]
    year = 1
    for index in range(len(population) - 1, 2, -1):
        if population[index] - population[index-1] < smallest:
            smallest = population[index] - population[index - 1]
            year = index
        else:
            continue
    return START_YEAR + year


# Function displays the results
def results(average, greatest, smallest):
    print('US Population Data (1950-1990)')
    print(f'Average Annual Change: {average:,.2f}')
    print(f'Year with Greatest Increase: {greatest}')
    print(f'Year with Smallest Increase: {smallest}')


if __name__ == '__main__':
    main()
