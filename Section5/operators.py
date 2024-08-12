# start: 0 , stop: 11 (excluded) step: 2
#for num in range(0,11,2):
#    print(num)

# index_count = 0
# word = 'abcde'
# for letter in word:
#     print(word[index_count])
#     index_count+=1

# Code below is effecient version of line 5 till 9
word = 'abcde'
for item in enumerate(word):
    print(item)

# for individual elements
for pos,letter in enumerate(word):
    print(pos)
    print(letter)
    print("\n")

my_list1 = ['a', 'b', 'c']
my_list2 = [100, 200, 300]
my_list3 = ["ä", "ö","ü" ]

for item in zip(my_list1, my_list2, my_list3):
    print(item)
print('x' in [1,2,3])
print('a' in 'a world')
print('my_key' in {'my_key':556})
print(min(my_list2))
print(max(my_list2))

#Random library
from random import  shuffle
my_list4 = [1,2,3,4,5,6,7,8,9,10]
shuffle(my_list4)
print(my_list4)

from random import randint
print(randint(0,100))
num = randint(0,10)
print(num)

result = input("What is your name? \n")
print(f'Hi {result}')

result = int(input("Favourite number? \n"))
print(f'Your favourite number is {result}')
print(type(result))
