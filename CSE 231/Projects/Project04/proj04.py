###############################################################################
#  Computer Project #4  
#  AWI File Analysis
#
#  This program reads a file containing infromation regarding to the National
#  Average Wage Index (AWI). It then analyzes the income ranges, what 
#  percent of the working population lie in the range, and what the average 
#  income in the range is. From this the program will prompt the user to decide
#  which relevant infromation to extract and display.
#  
# Program:
#  call function to open file
#  loop prompt to open file until user enters a valid file name
#  return year associated with file and the file
#  call function to read the file and store info in lists within one large list
#  call function to return the average income in the file using the list data
#  call function to return the median income in the file using the list data
#  display year, average, and function
#  display prompt asking if user wants values plotted
#  if yes:
#   call function to store lowest 40 income ranges (x-values) in a list
#   call function to store the cumulative percentages associated w/ the x-vals
#   call function to plot x-vals, y-vals, and year
#  loop prompt to ask user to get a range, percent, or quit
#  if range is selected:
#   prompt for a percent to input and check if it is a valid choice
#   call function to return the income range, cumulative percent, and avg income for the given percent
#   display what percent of incomes are bellow the income corresponding to the given percent
#  if percent is chosen:
#   prompt for a salary for the user to input and check if it is valid
#   call function to return the income range and cumulative percent of people below given salary
#   display what percentage of incomes are below the given salary
#  if something else is inputted:
#   display error
#  re-prompt user for a choice, quit if nothing is entered
##############################################################################

import pylab

BOTTOM_RANGE = 0 # Floor of income range
TOP_OF_RANGE = 2 # Ceiling of income range
POP_IN_RANGE = 3 # Population in income range
CUMULATIVE_POP = 4 # Cumulative population
CUMULATIVE_PERCENT = 5 # Cumulative percent
COMBINED_INCOME = 6 # Combined income of people in range
AVG_INCOME = 7 # Average income of people in the range

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    """ 
   Opens a file based on user input and returns the file pointer and year.

   Prompts the user to enter a year and attempts to open a file with the given
   year. If the file is successfully opened, the file pointer is returned.
   If the file is not found (FileNotFoundError), an error message is printed.
   The function loops to re-prompt the user for a new file. If the user 
   does not input a valid year an error message is displayed and the function 
   loops once more. If the user inputs something other than a year (ValueError) 
   an error message is displayed and the function loops again.   
   
   Returns:
       fp (file pointer): The file pointer if the file is successfully opened.
       year_check: The year inputted by user as an integer.
       
   Raises:
       FileNotFoundError: If the entered year is not found.
       ValueError: If the entered year cannot be converted to an integer.
   """
    LOWER_LIMIT = 1990 # Lower limit of years
    UPPER_LIMIT = 2023 # Upper limit of years
    # Will continue to ask user for file name until one can open
    while True:
        year_str = input("\nEnter a year where 1990 <= year <= 2023: ")
        filename = 'year'+year_str+'.txt' # Creates proper formatting
        
        try:
            year_check = int(year_str) # Converts year into an int
            
            # Checks if years fall into the accepted range 
            if year_check < LOWER_LIMIT or year_check > UPPER_LIMIT: 
                print("\nError in year. Please try again.")
                continue # Restarts open_file()
                
        except ValueError: # Displays error if year_check is not a number
            print("\nError in year. Please try again.")
            continue # Restarts open_file()
        
        try:
            fp = open(filename, 'r') # Attempts to open a file
            return fp, year_check
        
        except FileNotFoundError:
            print("\nError in file name:",filename," Please try again.")  
            continue # Restarts open_file()
        
def read_file(fp):
    """
    Reads a file and stores the information into a list.
    
    Creates an empty list to store lines of the file. The header lines are then
    skipped to have proper formatting. Next, the fp is iterated line by line. 
    Each line is striped of white space and commas are removed. Then the line 
    is split so each value will be its own element in a list. Next, the 
    list containing all the elements of the line is appended to list_of_lists. 
    Once all lines have been iterated and put into lists the list_of_lists 
    containing all the lists is returned.
    
    Args:
        fp: File pointer.
    Returns:
        list_of_lists: Data from fp organized into a list. 
    """
    list_of_lists = []
    
    # Skips header lines 
    for _ in range(2): 
        next(fp, None)
        
    # Iterates through  each line of the file    
    for line in fp: 
        # Removes white space, commas, and seperates elements of the line
        list_of_lists.append(line.strip().replace(',','').split())
    
    return list_of_lists
    
def find_average(data_lst):
    """
    Finds the average income by adding up the combined income of each range 
    divided by the total population with an income.
    
    Creates a variable which tracks the combined income of each range
    by iterating through data_lst. Then the last row and index are isolated
    to find the total number of people in all ranges. The total combined income
    is then divided by the total population to generate the average income.
    
    Args:
        data_lst: List containing lists of income data.
    Returns:
        average: Average income.  
    """
    total_income = 0 # Initializes income tracker
    
    # Iterates over each line in data_lst
    for line in data_lst:
        # Converts combined income to a float
        total_income += float(line[COMBINED_INCOME]) 
        
    # Concerts total population to a float    
    total_pop = float(data_lst[-1][CUMULATIVE_POP]) 
    average = total_income/total_pop 
    return average
 
def find_median(data_lst):
    """
    Finds the median income by locating the data line whose comulative percent
    is closest to 50% and returning the average income listed on that line.
    
    Initializes the target value as 50 which represents 50% (the median). Also
    initialize the closest difference with a large value to ensure it will be
    updated. Iterate over each line in the data list and calculate the 
    difference between the cumulative percent in the current line and the 
    target value. If the difference is smaller than the closest difference then
    the median will be updated with the average income in the current line and 
    the closest difference will be updated with the current difference. Once
    data list has been fully iterated the median income value will be returned.
    
    Args:
        data_lst: List containing lists of income data.
    Returns:
        median: Average income with the closest cumulative percent to 50%.
    """
    target = 50 # Goal percent to find median
    closest_diff = 10**6 # Initialize the closest difference with a big value
    
    # Iterates over each line in data_lst
    for line in data_lst:
        
        # Calculate the difference between the cumulative percent and the goal
        difference = abs(float(line[CUMULATIVE_PERCENT]) - target) 
        
        # Check if the current difference is less than the closest difference
        if difference < closest_diff: 
            
            # Update median with the average income in the current line
            median = float(line[AVG_INCOME]) 
            
            closest_diff = difference # Update the closest difference
    
    return median
        
def get_range(data_lst, percent):
    """
    Finds the income range, cumulative percent, and average income for a given
    percent.
    
    Iterates over data_lst until it finds a cumulative percent which is greater
    than or equal to the given percent. When one is found the income range,
    cumulative percent, and average income is stored in values which is then
    returned.
    
    Args:
        data_lst: List containing lists of income data.
        percent: Specified user inputted percent
    Returns:
        values: Tuple containing income range, cumulative percent, and average
            income for the income range for a given percent.
    """
    # Iterates over each line in data_lst
    for line in data_lst:
        # Converts the cumulative percent value to a float
        current_percent = float(line[CUMULATIVE_PERCENT])
        
        # Check if the current percent is greater than or equal to goal percent
        if current_percent >= percent:
            # Create a tuple containing the income range values, cumulative 
            # percent, and average income converted to floats.
            values = ((float(line[BOTTOM_RANGE]),float(line[TOP_OF_RANGE])), 
                float(line[CUMULATIVE_PERCENT]), float(line[AVG_INCOME]))
            return values 

def get_percent(data_lst,salary):
    """
    Finds the income range and cumulative percent of people in that range and
    below for a given salary.
    
    Iterates over data_lst until it finds a matching income range for the
    salary. Then store the income range and cumulative percent of people in
    the range into a tuple called values then return values.
    
    Args:
        data_lst: List containing lists of income data.
        salary: Specified user inputted salary.
    Returns:
        values: Tuple containing income range and cumulative percent of people
            in the income range and lower for a given salary.
    """
    # Iterates over each line in data_lst
    for line in data_lst:
        # Checks if salary is inbetween the income ranges
        if float(line[BOTTOM_RANGE]) <= salary <= float(line[TOP_OF_RANGE]):
          # Create a tuple containing the income range values and cumulative 
          # percent and converts them into floats.
          values = ((float(line[BOTTOM_RANGE]),float(line[TOP_OF_RANGE])), 
                    float(line[CUMULATIVE_PERCENT])) 
          return values
    
def get_x_vals (data_lst):
    """
    Gets x values for the graph by storing the bottom range of the lowest 40 
    income ranges into a list.
    
    Iterates through the first 40 lines of data_lst and appends the bottom
    income range to x_list after its converted to a float. Once the 40 lines
    have been iterated x_list is returned.
    
    Args:
        data_lst: List containing lists of income data
    Returns:
        x_list: List containing the 40 lowest income ranges in data
    """
    x_list = []
    for i in range(40): # Iterates the lowest 40 incomes in data_lst
        # Get the line at index i from data_lst
        line = data_lst[i]
        
        # Extract the bottom range income from the line and convert it to float
        x_list.append(float(line[BOTTOM_RANGE]))
        
    return x_list
    
def get_y_vals (x_vals, data_lst):
    """
    Gets the y values for the graph by storing the cumulative percentages
    associated with the income values in x_values.
    
    Iterates through the length of x_vals and appends the cumulative percent
    that corresponds to the x_val to y_list after the percent is converted into
    a float. Once this is accomplished y_list is returned.
    
    Args:
        x_vals: List containing the 40 lowest income ranges in data
    Returns:
        y_list: List containing the commulative percent of people in x_vals
    """
    y_list = []
    for i in range(len(x_vals)): # Iterates through the length of x_vals
        # Get the line at index i from data_lst
        line = data_lst[i]
        
        # Extract the cumulative percent from the line and convert it to float
        y_list.append(float(line[CUMULATIVE_PERCENT]))
        
    return y_list

def main():
    UPPER_PERCENT = 100
    LOWER_PERCENT = 0
    LOWER_SALARY = 0
    
    # Open a file and retrieve the file pointer and year
    fp, year = open_file()
    
    # Read and store data from file into a list
    data = read_file(fp)
    
    # Find the mean income from the data
    avg = find_average(data)
    
    # Find the median income from the data
    median = find_median(data)

    # Print the header
    print("\n{:6s}{:15s}{:15s}".format("Year","Mean","Median"))
    
    # Print the values for the current year, mean income, and median income
    print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year,avg,median))
    
    # Prompt user to determine if they want to graph values
    response = input("Do you want to plot values (yes/no)? ")
    
    # If input is yes, proceed with plotting the values
    if response.lower() == 'yes':
        # Retrieve x-values from the data
        x_vals = get_x_vals(data)
        
        # Retrieve the y-values which correspond to the x-values using the data
        y_vals = get_y_vals(x_vals, data)
        
        # Graph the x and y values
        do_plot(x_vals, y_vals, year)
    
    # Prompt user to choose either a range, percent, or quit program
    choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    
    # Continue loop until user enters nothing
    while choice:
        if choice == 'r':
            # Prompt for a percent value
            percent = float(input("\nEnter a percent: "))
            
            # Check if percent is within the valid range
            if percent > UPPER_PERCENT or percent < LOWER_PERCENT:
                print("\nError in percent. Please try again")
            else:
                # Get the income data for the inputted percent
                income_data = get_range(data, percent)
                
                # Get the income from the income_data tuple
                income = income_data[0][BOTTOM_RANGE]
                
                # Display the highest bottom range income below the percent
                print("\n{:4.2f}% of incomes are below ${:<13,.2f}."
                      .format(percent, income))

        elif choice == 'p':
            # Prompt the user for an income
            salary = float(input("\nEnter an income: "))
            
            # Checks to see if income is positive
            if salary < LOWER_SALARY:
                print("\nError: income must be positive")
            else:
                # Get the percentage data for the inputted salary
                percent_data = get_percent(data, salary)
                
                # Get the percent from the percent_data tuple
                percent = percent_data[1]
                
                # Display what percentage of incomes are below the given salary
                print("\nAn income of ${:<13,.2f} is in the top {:4.2f}% of incomes."
                      .format(salary, percent))
        else:
            # Error message for invalid user input
            print("\nError in selection.")
        
        # Re-prompt the user for a choice
        choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")

if __name__ == "__main__":
    main()