import string

def build_wordlist(fp):
    word_list = []
    reader = fp.read()
    for word in reader.split():
        for char in string.punctuation:
            word = word.replace(char, '')
        word_list.append(word.replace(string.punctuation,'').strip())
    return word_list
    
def find_unique(word_list):
    unique_list = []
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list

def main():
    infile = open("test.txt", 'r') 
    word_list = build_wordlist(infile)    
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)
if __name__ == "__main__":
    main()