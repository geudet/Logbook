a = [66.25, 333, 333, 1, 1234.5]

#insert "-1" at index 2
#add "333" at the end of list
a.insert(2, -1)
a.append(333)
print(a)

#the first index of "333"
print(a.index(333))

#remove "333"
a.remove(333)
print(a)

#sort the list
a.sort()
print(a)
