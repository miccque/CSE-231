STRING_FORMAT = "{:10s} {:<10d}"

def open_file(my_dict):
    with open("data1.txt", "r") as file_one, open("data2.txt", "r") as file_two:
        next(file_one)
        next(file_two)

        temp_list = [line.split() for line in file_one]
        build_dict(my_dict, temp_list)

        temp_list = [line.split() for line in file_two]
        build_dict(my_dict, temp_list)

        build_list(my_dict)
        
def build_dict(my_dict,temp_list):
    for index in range(len(temp_list)):
        if  temp_list[index][0] not in my_dict:
            my_dict [temp_list[index][0]] = int(temp_list[index][1])
        
        elif temp_list[index][0] in my_dict:
            my_dict [temp_list[index][0]] += int(temp_list[index][1])

def build_list(my_dict):
    list_of_scores = [] 
    for name,score in my_dict.items():
        list_of_scores.append((name,score))
    list_of_scores.sort()
    display_info(list_of_scores)
    
def display_info(list_of_scores):
    print("{:10s} {:<10s}".format("Name", "Total"))
    for item in list_of_scores:
        print(STRING_FORMAT.format(item[0], item[1]))

def main():
    my_dict = dict()
    file_reader = open_file(my_dict)
    
main()