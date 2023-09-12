def add_to_dict(dictt, key, value):
    if key in dictt.keys():
        print("Error. Key already exists.")
    else:
        dictt[key] = value
    return dictt
    
def remove_from_dict(dictt, key):
    try:
        dictt.pop(key)
    except KeyError:
        print("No such key exists in the dictionary.")
    return dictt
    
def find_key(dictt, key):
    try:
        print("Value: ", dictt[key])
    except KeyError:
        print("Key not found.")
        
def main():
    more = True
    dictt = {}
    dictlst = []
    while more:      
        print("Menu: ")
        choice = input("add(a), remove(r), find(f): \n")
        if choice.lower() == "a":
            key = input("Key: \n")
            value = input("Value: \n")
            dictt = add_to_dict(dictt, key,value)
        elif choice.lower() == "r":
            key = input("key to remove: \n")
            dictt = remove_from_dict(dictt,key)
        elif choice.lower() == "f":
            key = input("Key to locate: \n")
            find_key(dictt,key)
        else:
            print("Invalid choice.")
            
        do_more = input("More (y/n)? \n")
        if do_more.lower() != 'y':
            more = False
    if dictt:
      for key, value in dictt.items():
          temp = (key,value)
          dictlst.append(temp)
      print(sorted(dictlst))
main()