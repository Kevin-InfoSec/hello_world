#!/usr/bin/env python3
#Understanding mutable values using lists
import copy
def iterateThroughList(whichList):
    for i in range(len(whichList)):
        print('Index ' + str(i) + ' in your list is: ' + str(whichList[i]))

print("First we define a list myList[1,2,3]")
myList = [1,2,3]
iterateThroughList(myList)
print('Now let us make a new list newList equal to myList')
newList = myList
print('Because myList is mutable newList contains a pointer to the same place in memory')
print('This means modifying newList will also change myList, let us append 4 to newList')
newList.append('4')
print('Now let us check myList')
iterateThroughList(myList)
print('Even though we modified newList, myList is also changed')
print('Now let us use the copy.deepcopy function instead')
print('newList = copy.deepcopy(myList)')
newList = copy.deepcopy(myList)
print('Now newList has a new location in memory containing a copy of myList')
print('This means we can modify newList without effecting myList')
print('Let us append 5 to newList and print out both')
newList.append('5')
print('myList')
iterateThroughList(myList)
print('newList')
iterateThroughList(newList)
