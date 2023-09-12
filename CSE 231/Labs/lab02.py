
n_str = input("Input an integer (0 terminates): \n")

n = int(n_str)
odd_count = 0
even_count = 0
odd_sum = 0 
even_sum = 0
positive_int_count = 0

while n != 0:
    if n > 0:
        positive_int_count += 1
        if n%2 == 0:
            even_count += 1
            even_sum = n + even_sum
        else:
            odd_count += 1
            odd_sum = odd_sum + n
    n = int(input("Input an integer (0 terminates): \n"))
    

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
