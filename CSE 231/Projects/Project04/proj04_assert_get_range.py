from proj04 import read_file,get_range

fp = open("year2014.txt")
data_lst = read_file(fp)
data = get_range(data_lst,90)
instructor_data = ((90000.0, 94999.99), 90.80624, 92420.5)
print("Instructor data:", instructor_data)
print("Student data:", data)
assert data == ((90000.0, 94999.99), 90.80624, 92420.5)