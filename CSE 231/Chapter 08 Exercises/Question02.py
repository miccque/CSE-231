def sort_list(a_list):
    a_list.sort()

def main():
    user_input = input()
    a_list = []
    while user_input:
        a_list.append(int(user_input))
        user_input = input()
    
    ######Do not modify this part######
    print(a_list)
    sort_list(a_list)
    print(a_list)
    ######Do not modify this part######
    ######main() ends here
if __name__ == "__main__":
    main()