from proj03 import find_min_percent

line = "1        Gross domestic product                                A191RL1               3.1         0.2         3.3         5.2         5.6        -0.5        -0.2         5.4         4.6         5.6         3.2        -0.2         2.6        -1.9         4.6         7.3         4.2         3.5         3.5         4.2         3.7         1.9        -0.1         3.6         2.7         4.0         2.7         3.8         4.5         4.5         4.7         4.1         1.0         1.8         2.8         3.8         3.3         2.7         1.8        -0.3        -2.8         2.5         1.6         2.2         1.7         2.4         2.6"
min_val, min_val_index = find_min_percent(line)

if min_val_index == 40: #if student returns the column number in the data

    print("\nInstructor min value and index: {}, {}".format(-2.8,40))
    print("Instructor min value variable type: {}".format(type(-2.8)))
    print("\nStudent min value and index: {}, {}".format(min_val,min_val_index))
    print("Student min value variable type: {}".format(type(min_val)))
    assert (min_val,min_val_index) == (-2.8,40)

else: #if student returns the first character position in the line
    print("\nInstructor min value and index: {}, {}".format(-2.8,556))
    print("Instructor min value variable type: {}".format(type(-2.8)))
    print("\nStudent min value and index: {}, {}".format(min_val,min_val_index))
    print("Student min value variable type: {}".format(type(min_val)))
    assert (min_val,min_val_index) == (-2.8,556)
    


