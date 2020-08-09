name = input('Hello what is your name? ')
print('Hello ' + name + ' we are learning lists today!')
item = '0'
newList = []
while item.lower()!='done':
    print('What would you like to add to the list? Type done if you are finished')
    item = input()
    if item.lower()!='done':
        newList.append(item)
print('Your list is ')
for i in range(len(newList)):
    print('Index ' + str(i) + ' in your list is: ' + newList[i])
