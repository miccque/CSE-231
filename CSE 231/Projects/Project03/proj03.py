###############################################################################
#  Computer Project #3  
#  Gross Domestic Product File Analysis
#
#  This program reads a file containing infromation regarding a countries GDP.
#  It then analyzes the GDP percentage changes over the period from the file
#  and identifies the minimum and maximum percentage change values, along with
#  their respective years and GDP values. After extracting the relevant 
#  information it displays the results. 
#  
# Program:
#  function prompts for file and returns it if readable
#  extracts information on line containing years
#  use function to find the smallest percentage change value and its index
#  use function to find the largest percentage change value and its index
#  find the corresponding years to both min and max percentage change values
#  use the min and max percentage index to find their corresponding GDP value
#  convert GDP from billions to millions
#  display the minimal value, year and GDP, and the same three for maximum             
##############################################################################

#Formatted contansts to display the results
HEADER_FORMAT = "{:<10s}{:>8s}{:>6s}{:>18s}"
DATA_FORMAT = "{:<10s}{:>8.1f}{:>6d}{:>18.2f}"

def open_file():
    """ 
   Opens a file based on user input and returns the file pointer.
   
   Prompts the user to enter a file name and attempts to open the file
   If the file is successfully opened, the file pointer is returned.
   If the file is not found (FileNotFoundError), an error message is printed
   and the function calls itself to retry opening a file.

   Returns:
       fp (file pointer): The file pointer if the file is successfully opened.

   Raises:
       FileNotFoundError: If the entered file is not found.
   """
    while True: # Will continue to ask user for file name until one can open  
        
       file_name = input("Enter a file name: ") # Prompts user for a file
       
       try:
           fp = open(file_name, 'r') # Attempts to open a file
           return fp # Returns file
       
       except FileNotFoundError:
           # If file is not found displays error and process repeats
           print("\nError. Please try again")

def find_min_percent(line):
    """
    Finds the lowest GDP percentage change and its corresponding
    index in the given line.
    
    Iterates over the line in steps of 12 characters, starting from index 76
    and extracts a value from each iteration. Beginning at 76 and incramenting
    in steps of 12 helps to ensure proper formatting is maintained. This 
    extracted value is then attempted to be converted into a float. If 
    sucessful the value is compared to the current lowest value and if smaller 
    replaces the current min value. If the conversion is not successful the 
    iteration continues to the next step.
    
    Args:
        line: The line from the file containing GDP percentage changes.
    
    Returns:
        min_percent: Lowest GDP percentage change in the line.
        index_min: Index of the first character of where the lowest percentage 
            change occured.
    
    Raises:
        ValueError: If the extracted value cant be converted to a float.
    """
    min_percent = 10**6
    
    for index in range(76, len(line), 12): # Starts at 76 for proper formating
        
        value = line[index:index+12]
        
        try:
            # Converts value to float and removes white space
            value = float(value.strip())
        
            if value < min_percent:
                min_percent = value # Updates the current smallest value
                index_min = index # Updates largest value's indexed location
        
        except ValueError:
            # If value cannot be converted to a float the iteration continues
            continue
    
    return min_percent, index_min # Returns the smallest value and its index

def find_max_percent(line):
    """ 
    Finds the highest GDP percentage change and its corresponding index
    in a given line.
    
    Iterates over the line in steps of 12 characters, starting from index 76
    and extracts a value from each iteration. Beginning at 76 and incramenting
    in steps of 12 helps to ensure proper formatting is maintained. This 
    extracted value is then attempted to be converted into a float. If 
    sucessful the value is compared to the current largest value and if larger 
    replaces the current max value. If the conversion is not successful the 
    iteration continues to the next step.
    
    Args:
        line: The line from the file containing GDP percentage changes.
    
    Returns:
        max_percent: Largest GDP percentage change in the line.
        index_max: Index of the first character of where the largest percentage 
            change occured.
    
    Raises:
        ValueError: If the extracted value cant be converted to a float.
    """ 
    max_percent = 0
    
    for index in range(76, len(line), 12): # Starts at 76 for proper formating
        
        value = line[index:index+12] 
    
        try:
            # Converts value to float and removes white space
            value = float(value.strip())
        
            if value > max_percent:
                max_percent = value # Updates current largest value
                index_max = index # Updates largest value's indexed location
        
        except ValueError:
            # If value cannot be converted to a float the iteration continues
            continue 
    
    return max_percent, index_max # Returns the largest value and its index

def find_gdp(line, index):
    """
    Finds the GDP associated with a percentage change.
    
    Uses the indexed location of the GDP percentage change in a given year to 
    find the actual GDP of said year.
    
    Args:
        line: Line from file containing GDP values.
        index: Index of GDP percentage change for a specific year.
    
    Returns:
        gdp: GDP of year correlating to percentage change (in billions).
    """
    # Converts GDP to float and removes white space
    gdp = float(line[index:index+12].strip()) 
    return gdp
        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    """
    Displays the minimal value, year and GDP, and the same three for maximum
    """
    print("\n\nGross Domestic Product")
    print(HEADER_FORMAT.format('min/max','change','year','GDP (trillions)'))
    print(DATA_FORMAT.format('min', min_val,min_year,min_val_gdp))
    print(DATA_FORMAT.format('max',max_val,max_year,max_val_gdp))
    
def main():
    fp = open_file() #Retrieves a file
    
    count = 0 # Keeps track of lines
    
    for line in fp:
        count += 1 # Counter is incramented as line is incramented
        
        if count == 8: # Line containing number of years
            year_line = line # Stores line to reference later
            
        if count == 9: # Line containing GDP percentage changes
            # Finds min Δ% and its corresponding index
            min_percent, index_min = find_min_percent(line) 
            
            # Converts year to int and removes white space
            min_year = int(year_line[index_min:index_min+12].strip())
            
            # Finds max Δ% and its corresponding index
            max_percent, index_max = find_max_percent(line)
            
            # Converts year to int and removes white space
            max_year = int(year_line[index_max:index_max+12].strip())
            
        if count == 44: # Line containing GDP values
            min_gdp = find_gdp(line, index_min) # Finds GDP relating to min Δ%
            
            min_gdp = min_gdp/1000 # Converts min GDP to trillions
            
            max_gdp = find_gdp(line, index_max) # Finds GDP relating to max Δ%
            
            max_gdp = max_gdp/1000 # Converts max GDP to trillions
    
    # All important values are sent to be displayed
    display(min_percent, min_year, min_gdp, max_percent, max_year, max_gdp)

if __name__ == "__main__":
    main()
