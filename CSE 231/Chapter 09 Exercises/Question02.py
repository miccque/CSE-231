dict_of_words = {}

def open_file():
    fpointer = open('example.txt')
    return fpointer

def main():
    dictlist = []
    fp = open_file()
    for line in fp:
        word_list = line.lower().replace(',','').split()
        for word in word_list:
            if word in dict_of_words:
                dict_of_words[word] += 1
            else:
                dict_of_words[word] = 1
    for key, value in dict_of_words.items():
        temp = (key,value)
        dictlist.append(temp)
    print(sorted(dictlist))
    
main()