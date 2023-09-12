from proj04 import read_file,find_average

fp = open("year2014.txt")
data_lst = read_file(fp)
avg = find_average(data_lst)
avg = round(avg)
print("Instructor Avg: ", 44569)
print("student Avg: ", avg)
assert avg == 44569