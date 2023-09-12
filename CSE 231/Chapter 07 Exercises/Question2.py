def return_list(the_string):
    if ',' not in the_string and ' ' not in the_string:
        return the_string
    else:
        return the_string.replace(',', ' ').strip().split()
    
def main():
    the_string = input("Enter the string: \n")
    result = return_list(the_string)
    print(result)
    
main()