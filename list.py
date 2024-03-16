
#list are mutable means we can change value in it


#list
countries =['uk','usa','india','germany','brazil']
print(countries)
print(countries[0])
print(countries[2][0])
print(countries[1:])
print(countries[1:3])
print(countries[2:3])

print(type(countries))

countries[0]='canda'
print(countries)

print(countries[-2])

print(countries[2])

#2nd way of list
name = list(('rahul','debasis'))
print(name)

#to extend
list1 = [3,3,34,56,6,4,3]
list2 = ['kiwi','allo','pyazz']
list1.extend(list2)
print(list1)

#to append
list1.append(43343)
print(list1)

#to put in between the list
list2.insert(1,'cherry')
print(list2)

#to remove
list2.remove('kiwi')
print(list2)

#to clear all list item
list2.clear()
print(list2)

#to print ndex no of item in list
list2=['kiwi','cherry','banana','kiwi']
print(list2.index('kiwi'))
print(list2.count('kiwi'))

list2.pop()
print(list2)

#to delete list
list3 = [23,22,232,3,1,3]
del list3
print(list3)