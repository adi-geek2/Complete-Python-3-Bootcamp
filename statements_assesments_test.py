st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

for i in range(0,11,2):
        print(i)

div_by_3 = [i for i in range(0,50) if i % 3 == 0]
print(div_by_3)

for word in st.split():
    if len(word) % 2 == 0:
        print(word)

for num in range(0,101):
    if  num % 15 == 0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif  num % 3 == 0:
        print('Fizz')
    else:
        print(num)

st = 'Create a list of the first letters of every word in the string'
list_of_first_letters =  [word[0] for word in st.split()]
print(list_of_first_letters)
