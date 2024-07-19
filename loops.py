mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 == 0:
        print("Even number:" + str(num))
    else:
        print("Odd number:" + str(num))
print("Two element tuple:")
tup = (1,2,3)
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10)]
len(mylist)
for a,b in mylist:
    print(a)
mylist2 = [(1,2,3),(4,5,6),(7,8,9)]
print("Three element tuple:")
for a,b,c in mylist2:
    print(b)
print("Dictionary: ")
d = {'k1':1, 'k2': 2, 'k3':3} 
for item in d.values():
    print(item)   
