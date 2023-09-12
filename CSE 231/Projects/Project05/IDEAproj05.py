from operator import itemgetter

#Use the following in your input and print statements
"Enter a file: "
"\nError in file name: {}. Please try again."
"State"
"Max Year"
"Max"
"Min Year"
"Min"
"\nCrop: {}"


#Use these constants to format your output table
HEADER_FORMAT = "{:<20s}{:>10s}{:>6s}{:>10s}{:>6s}" #state, max year, max value, min year, min value in this order
DATA_FORMAT = "{:<20s}{:>10s}{:>6d}{:>10s}{:>6d}"   #state, max year, max value, min year, min value in this order

CROPS = []
STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def open_file():
    '''You fill in the doc string'''
    while True:
        #file_name = input("Enter a file: ")
        try:
            #fp = open(file_name)
            fp = open('alltablesGEcrops.csv')
            return fp
        except FileNotFoundError:
            #print("\nError in file name: {}. Please try again.".format(file_name))
            pass
        
def read_file(fp,state_dict):
    '''You fill in the doc string'''
    fp.readline()
    for line in fp:
        line_lst = line.strip().split(',')
        state = line_lst[0].strip()
        crop = line_lst[1]
        variety = line_lst[3]
        year = line_lst[4]
        value = line_lst[6]
        
        if crop not in CROPS:
            CROPS.append(crop)
        
        if state in STATES:
            if variety == "All GE varieties" and value.isdigit():
                add_state(state,crop,year,int(value),state_dict)

def add_state(state,crop,year,value,state_dict):
    #NOTE: {State: {Crop: Max Year, Max Val, Min Year, Min Val}}
    MAX_PLACEHOLDER = 0 
    MIN_PLACEHOLDER = 10**6

    if state not in state_dict:
        state_dict[state] = {}
    
    if crop not in state_dict[state]:    
        state_dict[state][crop] = {'Max Year': '','Max': MAX_PLACEHOLDER,
                                   'Min Year': '', 'Min': MIN_PLACEHOLDER}
        
    if value > state_dict[state][crop]['Max']:
        state_dict[state][crop]['Max'] = value
        state_dict[state][crop]['Max Year'] = year
    
    if value < state_dict[state][crop]['Min']:
        state_dict[state][crop]['Min'] = value
        state_dict[state][crop]['Min Year'] = year
        
def display_dict(state_dict):
    CROPS.sort()
    for crop in CROPS:
        print("\nCrop: {}".format(crop))
        print(HEADER_FORMAT.format("State", "Max Year", "Max", "Min Year", "Min"))
        for state in STATES:
            try:
                print(DATA_FORMAT.format(
                    state,state_dict[state][crop]["Max Year"], 
                    state_dict[state][crop]["Max"], 
                    state_dict[state][crop]["Min Year"],
                    state_dict[state][crop]["Min"])
                    )  
            except KeyError:
                pass
            
def main():
    fp = open_file()
    state_dict = {}
    read_file(fp,state_dict)
    display_dict(state_dict)
    #print(state_dict)
   
if __name__ == "__main__":
    main()