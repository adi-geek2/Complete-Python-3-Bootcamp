def myfunc(word):
    output = " "
    for count in range(0,len(word)):
        if count % 2 == 0:
            output = output + word[count].upper()
            print(f"even :{count} is {word[count]}")
        else:
            output = output + word[count].lower()
            print(f"odd :{count} is {word[count]}")
    return output

print(myfunc("sdjkfhsjkdfhsd"))
