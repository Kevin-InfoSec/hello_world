#!/usr/bin/env python3
print('Dictionaries are UNORDERED and MUTABLE key/value pairs.')
print('The syntax for a dictionary is dictionary = {key1:value1,key2:value2,...keyX:valueX}')
print('Let us define a new dictionary for our cats attributes')
print('''Our syntax is newDict = {'name':'pixel','color':'grey','disposition':'cuddle slut'}''')
newDict = {'name':'pixel','color':'grey','disposition':'cuddle slut'}
print(str(newDict))
print("\n\n We can use in/not in to determine if a KEY (not a value) is in the dictionary")
print("'name' in newDict")
print('name' in newDict)
print("'pixel' in newDict")
print('pixel' in newDict)
print("\n\n We can call values with newDict[key]")
print('However, if we use a key not present it will throw an error')
print('We can avoid this using the get function, systax newDict.get(key, valueToReturnIfKeyNotPresent)')
print("Example: newDict.get('name', '')")
print(newDict.get('name', ''))
print("Example: newDict.get('age', '0')")
print(newDict.get('age', '0'))
print('This is particulaly useful for non-static lists')
partySupplies = ''
supplyQuantity = '0'
partyDict = {}
while partySupplies.lower() != 'done':
    print('What are you bringing to the party? Type done to finish')
    partySupplies = input()
    if partySupplies != 'done':
        supplyQuantity = input('How many ' + partySupplies + ' are you bringing?')
        partyDict[partySupplies] = supplyQuantity
supplyCheck = ''
while supplyCheck.lower() != 'done':
    print('What supplies are you checking? Type done to finish')
    supplyCheck = input()
    if supplyCheck != 'done':
        print('You are bringing ' + str(partyDict.get(supplyCheck, 0)) + ' ' + supplyCheck + ' to the party')
        
print("\n\n Dictionary functions .keys(), .values(), .items() return lists of the keys, values, and both")
print('We can use multi-variable assignment to return a list of key/value pairs')
print("for k,v in newDict.items() \n\t print(k,v)")
for k,v in newDict.items():
    print(k,v)
    
