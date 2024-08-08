def print_list(my_string:list):
    for letter in my_string:
        print(letter)
    print("\n")

my_string = 'hello'
my_list = []

#for letter in my_string:
#    my_list.append(letter)

my_list = [letter for letter in my_string]
print_list(my_list)
my_list = [num**2 for num in range(0,10)]
print_list(my_list)
my_list = [num**2 for num in range(0,10)if num % 2 == 0]
print_list(my_list)
celsius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp +32) for temp in celsius]
print_list(fahrenheit)
results = [x if x % 2 == 0 else 'ODD' for x in range(0,10)]
print_list(results)
# nested loop compreshesnion
my_list = [x*y for x in [2,4,5] for y in [200,300,500]]       
print_list(my_list)
