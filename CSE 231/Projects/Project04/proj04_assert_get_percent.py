from proj04 import read_file,get_percent

fp = open("year2014.txt")
data_lst = read_file(fp)
data = get_percent(data_lst,150000)
instructor_data = ((150000.0, 154999.99), 96.87301)
print("Instructor data:", instructor_data)
print("Student data:", data)
assert data == ((150000.0, 154999.99), 96.87301)