from proj03 import find_gdp,find_max_percent,find_min_percent

line9 = "1        Gross domestic product                                A191RL1               3.1         0.2         3.3         5.2         5.6        -0.5        -0.2         5.4         4.6         5.6         3.2        -0.2         2.6        -1.9         4.6         7.3         4.2         3.5         3.5         4.2         3.7         1.9        -0.1         3.6         2.7         4.0         2.7         3.8         4.5         4.5         4.7         4.1         1.0         1.8         2.8         3.8         3.3         2.7         1.8        -0.3        -2.8         2.5         1.6         2.2         1.7         2.4         2.6"
line44 = "1        Gross domestic product                                A191RC1            1019.9      1075.9      1167.8      1282.4      1428.5      1548.8      1688.9      1877.6      2086.0      2356.6      2632.1      2862.5      3211.0      3345.0      3638.1      4040.7      4346.7      4590.2      4870.2      5252.6      5657.7      5979.6      6174.0      6539.3      6878.7      7308.8      7664.1      8100.2      8608.5      9089.2      9660.6     10284.8     10621.8     10977.5     11510.7     12274.9     13093.7     13855.9     14477.6     14718.6     14418.7     14964.4     15517.9     16155.3     16691.5     17393.1     18036.6"


min_val, min_val_index = find_min_percent(line9) 
min_val_gdp = find_gdp(line44, min_val_index)
print("="*20)
print("\nInstructor GDP with minimum change: {}".format(14418.7))
print("Instructor variable type: {}".format(type(14418.7)))
print("\nStudent GDP with minimum change: {}".format(min_val_gdp))
print("Student variable type: {}".format(type(min_val_gdp)))  
assert min_val_gdp == 14418.7

print("="*20)
max_val, max_val_index = find_max_percent(line9)
max_val_gdp = find_gdp(line44, max_val_index)
print("\nInstructor GDP with max change: {}".format(4040.7))
print("Instructor variable type: {}".format(type(4040.7)))
print("\nStudent GDP with max change: {}".format(max_val_gdp))
print("Student variable type: {}".format(type(max_val_gdp)))  
assert max_val_gdp == 4040.7

