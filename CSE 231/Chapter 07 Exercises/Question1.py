def new_list_function(initial_list):
    return initial_list * 3

def main():
    initial_list = [] 
    while True:
        input_str = input('Enter value to be added to list: \n')
        if input_str.lower() == 'exit':
            break
        initial_list.append(input_str)
    new_list = new_list_function(initial_list)
    for item in new_list:
        print(item)
    
main()
    
