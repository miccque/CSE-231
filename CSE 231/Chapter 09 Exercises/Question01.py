the_dict = {}
dictlist = []
name = input("Name: \n")
num = input("Number: \n")
the_dict[name] = num

ask = input('More data (y/n)? \n')

while ask != 'n':
    name = input("Name: \n")
    num = input("Number: \n")
    the_dict[name] = num
    ask = input('More data (y/n)? \n')

for key, value in the_dict.items():  #we store the dictionary in a list, then sort and print
    temp = (key,value)
    dictlist.append(temp)       
print(sorted(dictlist))
