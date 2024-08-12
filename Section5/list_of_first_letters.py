st = 'Create a list of the first letters of every word in the string'
list_of_first_letters =  []
for word in st.split():
    list_of_first_letters.append(word[0])
print(list_of_first_letters)
