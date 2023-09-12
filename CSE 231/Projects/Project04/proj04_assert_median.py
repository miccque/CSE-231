from proj04 import read_file,find_median

fp = open("year2014.txt")
data_lst = read_file(fp)
median = find_median(data_lst)
median = round(median)
print("Instructor Median: ", 27457)
print("Student Median: ", median)
assert median == 27457