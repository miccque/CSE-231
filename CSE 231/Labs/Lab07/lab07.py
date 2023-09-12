import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 
              'Leisure/hospitality', 'Manufacturing']

def read_file(fp):

    list_of_lists = []
    reader = csv.reader(fp)
    
    for _ in range(4): # Skips header
        next(reader, None) 
        
    counter = 0
    for line in reader:
        counter += 1
        if counter == 2:
            continue # Skips blank row
        list_of_lists.append(line) # Puts everything into a list for refrence
    print(list_of_lists)    
    return list_of_lists

def get_totals(L):

    total_val = []
    for index in L[1:]: 
        total_val.append(int(index[1].strip('<').replace(',','')))
        
    total_val = sum(total_val)
    return int(L[0][1].replace(',','')), total_val

def get_industry_counts(L):

    industry_counts = [0, 0, 0, 0, 0]
    
    for service in L[1:]:
        if service[9] in INDUSTRIES:
            x = INDUSTRIES.index(service[9]) 
            industry_counts[x] += 1
    
    agriculture = ['Agriculture', industry_counts[0]]
    business = ['Business services', industry_counts[1]]
    construction = ['Construction', industry_counts[2]]
    leisure = ['Leisure/hospitality', industry_counts[3]]
    manufacturing = ['Manufacturing',  industry_counts[4]]
    return_list = sorted([agriculture,business,construction,leisure,
                   manufacturing], key=itemgetter(1))
    return_list.reverse()
    return return_list

def get_largest_states(L):

    largest_states = []
    us = float(L[0][2].strip('%'))
    
    for num in L[1:]:
        check = float(num[2].strip('%'))
        if check > us:
            largest_states.append(num[0])
    return largest_states

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()
