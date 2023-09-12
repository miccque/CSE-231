###############################################################################
#  Computer Project 5  
#  Adoption of Genetically Modified crops in the U.S. - File Analysis
#
#  This program reads a file containing GM crop data. It then analyzes the 
#  adoption of different GM food and non-food crops in different states. 
#  It then determines the minimum and maximum adoption by state and the years 
#  when the minimum and maximum occurred.
#  
# Constants:
#    HEADER_FORMAT (str): Format string for the header of the output table, 
#        specifying the order of columns (state, max year, max value, min year, 
#        min value).	
#    
#    DATA_FORMAT (str): Format string for displaying data in the output table, 
#        specifying the order of columns (state, max year, max value, min year, 
#        min value).
#    
#    CROPS (list): A list to store the names of crops.
#    
#    STATES (list): A list of state names in alphabetical order.
#
# Functions:
#    open_file(): Prompts the user to enter a file name and returns the file 
#        pointer if the file is successfully opened.
#    
#    read_file(fp, state_dict): Reads the data from the file and extracts 
#        relevant information to be processed and added to the state_dict.
#    
#    add_state(state, crop, year, value, state_dict): Updates the state-level 
#        data dictionary with the given state, crop, year, and percentage value.
#    
#    display_dict(state_dict): Displays the information stored in the state_dict, 
#        organized by crop and state.
#    
#    main(): Entry point of the program, opens the file, creates the state_dict, 
#        reads the file, and displays the results.            
##############################################################################



#Constants to format output table
HEADER_FORMAT = "{:<20s}{:>10s}{:>6s}{:>10s}{:>6s}" #state, max year, max value, min year, min value in this order
DATA_FORMAT = "{:<20s}{:>10s}{:>6d}{:>10s}{:>6d}"   #state, max year, max value, min year, min value in this order

CROPS = [] # List to store crops
STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def open_file():
    """ 
   Opens a file based on user input and returns the file pointer.
   
   Prompts the user to enter a file name and attempts to open the file If the 
   file is successfully opened, the file pointer is returned. If the file is 
   not found (FileNotFoundError), an error message is printed and the function 
   loops again.

   Returns:
       fp (file pointer): The file pointer if the file is successfully opened.

   Raises:
       FileNotFoundError: If the entered file is not found.
   """
    while True: # Will continue to ask user for file name until one can open
        file_name = input("Enter a file: ") # Prompts user for a file
        try:
            fp = open(file_name) # Attempts to open a file
            return fp # Returns file
        except FileNotFoundError:
            print("\nError in file name: {}. Please try again.".format(file_name))
        
def read_file(fp,state_dict):
    """
    Reads a file and extracts information to be processed and added to a dict.
    
    The header line is skipped to have proper formatting. Next, the fp is 
    iterated line by line. Each line is striped of white space the line 
    is split so each value will be its own element in a list. Next, specific
    data is extracted from the list and stored. Then the specific data is sorted 
    and those which pass are sent to the function add_state to be processed
    further.
    
    Parameters:
        fp: File pointer.
        state_dict: Dictionary for storing state level info.
    """
    fp.readline() # Skips header
    
    for line in fp: # Iterates through file line by line
        # Removes whitespace and seperates elements of line
        line_lst = line.strip().split(',') 
        state = line_lst[0].strip() # Removes whitespace surrounding state name
        crop = line_lst[1] # Retrieves the crop
        variety = line_lst[3] # Retrieves the variety of GE
        year = line_lst[4] # Retrieves the year
        value = line_lst[6] # Retrieves percent of crops planted
        
        if crop not in CROPS:
            CROPS.append(crop) # Adds the crop to the CROPS list if not present
        
        if state in STATES:
            if variety == "All GE varieties" and value.isdigit():
                # Calls a function to process information and add to the dict
                add_state(state,crop,year,int(value),state_dict)

def add_state(state,crop,year,value,state_dict):
    """
    Update the state-level data dictionary with the given state, crop, year, 
    and percentage value.
    
    If state is not present in the dictionary it creates a new entry with the
    state as a key. If the crop is not present under the state in the dictionary
    it adds a new entry for the crop along with placeholder values. If the
    value in the data is greater than the current max value for the crop it
    updates the max value and its corresponding year. If the value in the data 
    is less than the current min value for the crop it updates the min value 
    and its corresponding year. 
    
    Parameters:
        state: State name
        crop: Crop name
        year: Year of data
        value: Percent of crop planted
        state_dict: Dictionary to store data at the state level
    """
    MAX_PLACEHOLDER = 0 
    MIN_PLACEHOLDER = 10**6

    if state not in state_dict:
        # Create a dictionary for the state if it doesn't exist
        state_dict[state] = {} 
    
    if crop not in state_dict[state]:
        # Create a dictionary for the crop under the state
        # Format - {State: {Crop: Max Year: '', Max Val: '', Min Year: '', Min Val: ''}}
        state_dict[state][crop] = {'Max Year': '','Max': MAX_PLACEHOLDER,
                                   'Min Year': '', 'Min': MIN_PLACEHOLDER}
        
    if value > state_dict[state][crop]['Max']:
        state_dict[state][crop]['Max'] = value # Update the max value
        state_dict[state][crop]['Max Year'] = year # Update the max year

    
    if value < state_dict[state][crop]['Min']:
        state_dict[state][crop]['Min'] = value # Update the min value
        state_dict[state][crop]['Min Year'] = year # Update the min year
        
def display_dict(state_dict):
    """
    Displays the information stored in the dictionary by first displaying crop
    ordered in alphabetical order and for each crop the data is output 
    alphabetically by state name.
    
    Sorts the CROPS list to order crops in alphabetical order. Next iterate
    through the crops and display header line. Next iterate through the STATES
    list (which is already in alphabetical order) and attempt to display the
    values associated with the state and crop keys. If no such values exist it
    continues to the next state until all the states and crops are iterated.
    
    Parameters:
        state_dict: Dictionary for storing state info.
    
    Raises:
        KeyError: If key is not present
    """
    CROPS.sort() # Organizes CROPS in alphabetical order
    for crop in CROPS:
        print("\nCrop: {}".format(crop)) # Print the crop name
        print(HEADER_FORMAT.format("State", "Max Year", "Max", "Min Year", "Min"))
        
        for state in STATES:
            try:
                # Print the data format for each state and crop
                print(DATA_FORMAT.format(
                    state,
                    state_dict[state][crop]["Max Year"], 
                    state_dict[state][crop]["Max"], 
                    state_dict[state][crop]["Min Year"],
                    state_dict[state][crop]["Min"])
                    )  
            except KeyError:
                pass # Ignore KeyError and continue to the next state
            
def main():
    fp = open_file()  # Open the file and assign the file object to fp
    
    state_dict = {} # Create an empty dictionary to store state level data
    
    read_file(fp,state_dict) # Reads the data from the file and populates state_dict
    
    display_dict(state_dict) # Display the contents of the state_dict
   
if __name__ == "__main__":
    main()