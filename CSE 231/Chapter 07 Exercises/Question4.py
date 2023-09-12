def list_to_tuple(a_list):
    print(tuple(a_list))

def main():
    good = True
    new_list = []
    a_list = input("Enter elements of list separated by commas: \n").strip().split(',')
    for i in a_list:
        try:
            new_list.append(int(i))
        except ValueError:
            print("Error. Please enter only integers.")
            good = False
    if good == True:        
        a_list = new_list
        list_to_tuple(a_list)
        print(new_list)
    
main()