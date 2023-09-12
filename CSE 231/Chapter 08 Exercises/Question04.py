def game_of_eights(a_list):
    tracker = 0
    real_tracker = 0
    for index in a_list:
        try:
            if int(index) == 8:
                tracker += 1
            else:
                tracker = 0
            if tracker == 2:
                real_tracker = 1
        except ValueError:
            print('Error. Please enter only integers.')
            return
    if real_tracker == 1:
        print(True)
        return True
    print(False)
    return False

def main():
    a_list = input("Enter elements of list separated by commas: \n").split(',')
    result = game_of_eights(a_list)
main()

