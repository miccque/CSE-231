from proj03 import find_max_percent

line = "1        Gross domestic product                                A191RL1               3.1         0.2         3.3         5.2         5.6        -0.5        -0.2         5.4         4.6         5.6         3.2        -0.2         2.6        -1.9         4.6         7.3         4.2         3.5         3.5         4.2         3.7         1.9        -0.1         3.6         2.7         4.0         2.7         3.8         4.5         4.5         4.7         4.1         1.0         1.8         2.8         3.8         3.3         2.7         1.8        -0.3        -2.8         2.5         1.6         2.2         1.7         2.4         2.6"
max_val, max_val_index = find_max_percent(line)

if max_val_index == 15: #if student returns the column number in the data

    print("\nInstructor max value and index: {}, {}".format(7.3,15))
    print("Instructor max value variable type: {}".format(type(7.3)))
    print("\nStudent max value and index: {}, {}".format(max_val,max_val_index))
    print("Student max value variable type: {}".format(type(max_val)))
    assert (max_val,max_val_index) == (7.3,15)

else: #if student returns the first character position in the line
    print("\nInstructor max value and index: {}, {}".format(7.3,256))
    print("Instructor max value variable type: {}".format(type(7.3)))
    print("\nStudent max value and index: {}, {}".format(max_val,max_val_index))
    print("Student max value variable type: {}".format(type(max_val)))
    assert (max_val,max_val_index) == (7.3,256)
    
    
    

        
    


