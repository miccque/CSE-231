from operator import itemgetter

def build_map( in_file1, in_file2 ):
    data_map = {}
    
    in_file1.readline()
    in_file2.readline()

    for line in in_file1:

        # Split the line into two words
        continent_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        
        # Ignore empty strings
        if continent != "":
            # If current continent not in map, insert it 
            if continent not in data_map:
                data_map[continent] = {}
            
            # If country is not empty insert (continent is guaranteed to be in map)
            if country not in data_map[continent]:
                data_map[continent][country] = set()
            
                 # If current country not in map, insert it 

    for line in in_file2:       

        # Split the line into two words
        countries_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        
        # Ignore empty strings
        if country != "":
            
            # insert city (country is guaranteed to be in map)
            
            for continent in data_map:
                if country in data_map[continent] and city not in data_map[continent][country]:
                    data_map[continent][country].add(city)
    return data_map

def display_map( data_map ):

    # Modify this code to display a sorted nested dictionary
    continents_list = sorted(data_map.keys()) #sorted list of the continent keys
    
    for continent in continents_list: # For each continent
        print("{}:".format(continent)) #continents in continents_list
        countries_list = sorted(data_map[continent].keys()) #sorted list of the countries keys in the continents      
        for country in countries_list: # For each country
            print("{:>10s} --> ".format(country),end = '') #countries in countries_list
            cities = sorted(data_map[continent][country]) # For each city 
            for i, city in enumerate(cities): #As long as not last city, add a comma and a space after the cities names
                if i != len(cities) - 1:
                    print("{}, ".format(city), end='')
                else:
                    print("{}".format(city))

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
    data_map = {}
    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()