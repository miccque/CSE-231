import string
from operator import itemgetter


def add_word( word_map, word ):
    """
    Assigns the word as a key to the dictionary and inceases its value for each
    time the word is sent to add_word
    
    Checks if word is already a key in the dictionary. If it isnt the word is 
    added. Then the word's value is increased by one. 
    
    Args:
        word_map:
        word: Word in file
    """
    # If word isnt in the dict it adds it as a key and sets value to 0
    if  word not in word_map:
        word_map[ word ] = 0

        # Adds one to the value of whatever word that's already a key
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    """
    Breaks down each line of file into words before sending it to be added to
    the dictionary word_map.
    
    Indexes file by line and splits it so each word is its own element. Then
    each word is stripped of whitespace, punctuation, and capitalization before
    sent to the add_word function.
    
    Args:
        in_file: File pointer
        word_map: dictionary of words (keys) and their occurances (value) 
    """
    for line in in_file:

        # Indexes line of file so each word is its own element in the list
        word_list = line.split()

        for word in word_list:

            # Removes any whitespace and punctuation from a word and sends the
            # word to add_word to count its occurance/add it to the dict
            word = word.strip(' ').strip(string.punctuation).lower()
            if word:
                add_word( word_map, word )
        

def display_map( word_map ):
    """
    Adds the keys and values of world_map to a list and then sorts the values
    from greatest to smallest before printing the items.
    
    Args:
        word_map: Dictionary with words as keys and their occurances as values
    """
    word_list = list()

    # Takes the word and count from world_map and adds them into a list
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # Sorts the words from smallest to largest
    freq_list = sorted( word_list, key=lambda x: (-x[1], x[0]) )
    
    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    """
    Prompts user for a file and attempts to open it, returning the file if
    possible. 
    
    Returns:
        in_file: File pointer if it is able to open, else None
    Raises:
        IOError: If file is unable to open
    """
    try:
        file_name = input("Enter file name: ")
        in_file = open( "{}".format(file_name), "r")
        print() #keep it for testing purposes in Coding Rooms
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()
