def build_map(in_file1, in_file2):
    data_set = set()

    in_file1.readline()
    in_file2.readline()

    lines_in_file2 = in_file2.readlines()

    for line_one in in_file1:
        # Split the line into two words
        continent_list = line_one.strip().split()

        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()

        # Ignore empty strings
        if continent != "":
            # Add continent to the set
            first_tuple = (continent, country)

            cities = []
            for line_two in lines_in_file2:
                # Split the line into two words
                countries_list = line_two.strip().split()

                # Convert to Title case, discard whitespace
                country_two = countries_list[0].strip().title()
                city = countries_list[1].strip().title()

                if country_two == country and city not in cities:
                    cities.append(city)

            if cities:
                combined = first_tuple + tuple(cities)
                data_set.add(combined)
                
    return data_set



def display_map(data_set):
    # Sort the set
    sorted_map = sorted(data_set)

    current_continent = ""

    for entry in sorted_map:
        continent = entry[0]
        country = entry[1]
        cities = sorted(entry[2:])  # Retrieve all cities from the entry

        if continent != current_continent:
            print("{}:".format(continent))
            current_continent = continent

        print("{:>10s} --> ".format(country), end='')

        # Print all the cities on the same line
        for i, city in enumerate(cities): #As long as not last city, add a comma and a space after the cities names
            if i != len(cities) - 1:
                print("{}, ".format(city), end='')
            else:
                print("{}".format(city))

          # Print a new line after printing all the cities



def open_file():

    try:
        filename = input("Enter file name: ")
        print()
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():

    # YOUR CODE
    data_set = set()
    in_file1 = open('continents.txt', 'r')#open_file() #Continents with countries file: continents.txt
    in_file2 = open('cities.txt', 'r')#open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_set = build_map( in_file1, in_file2 ) # data_set is a dictionary
        display_map( data_set )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()
