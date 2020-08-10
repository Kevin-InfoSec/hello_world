#!/usr/bin/env python3
import re

print('''This regex tutorial assumes basic regex knowledge and will cover it's
application in Python. To use regular expressions you have to import the re module
regular expressions are a data type in Python so we will use the regular expression
re.compile() function, designed to recognize a phone number, to create a regular
expression. Because of the number of backslashes in regular expressions we generally
use raw strings (r'string') to define a regular expression. This means we special
characters like \n, \d will not be escaped

phoneNumRegex = re.compile(r'\(?(\d{3})\)?[- ]\d{3}-\d{4})\'''')
input('Press enter key to continue')
print('\n\n\n')
phoneNumRegex = re.compile(r'\(?(\d{3})\)?[- ](\d{3}-\d{4})')
print('We can use regexObject.searh() method to create a match object')
print("i.e. mo = phoneNumRegex.search('My number is 123-456-7890')")
mo = phoneNumRegex.search('My number is 123-456-7890')
print("We can then call the matchObject.group() method to get the match")
print('print(mo.group())')
print(mo.group())
input('Press enter key to continue')
print('\n\n\n')
print('''Regex objects can define groups with ()
i.e. phoneNumRegex = re.compile(r'\(?(\d{3})\)?[- ](\d{3}-\d{4})')
Now we can call mo.group(1) to get the area code and mo.group(2) to get the local number
Note: mo.group() will still return the full match
Note2: Our regex is designed to use two formats so this time we'll use the second
one (123) 456-7890''')
phoneNumRegex = re.compile(r'\(?(\d{3})\)?[- ](\d{3}-\d{4})')
mo = phoneNumRegex.search('Call me at (123) 789-4560')
print('''mo = phonenumberRegex.search('Call me at (123) 789-4560')
mo.group(1)''')
print(mo.group(1))
print('mo.group(2)')
print(mo.group(2))
print('mo.group()')
print(mo.group())
input('Press enter key to continue')
print('\n\n\n')
print('While the search() method returns the first match, the findall() method returns all matches')
print('Note: the findall() method will return each group match if groups are used, not the direct match')
print("phoneNumRegex.findall('I can be reached at p:123-456-7890 or c: 234-567-8901')")
print(phoneNumRegex.findall('I can be reached at p:123-456-7890 or c:234-567-8901'))    
print("Now let's try the same thing withphoneNumRegex = re.compile(r'\(?\d{3}\)?[- ]\d{3}-\d{4}')")     
phoneNumRegex = re.compile(r'\(?\d{3}\)?[- ]\d{3}-\d{4}')
print(phoneNumRegex.findall('I can be reached at p:123-456-7890 or c:234-567-8901'))
input('Press enter key to continue')
print('\n\n\n')
print("We can use the reg.sub() method to find/replace, or substitute values")
print("That syntax is regex.sub('replaceWithThis', 'inThis")
print("i.e. phoneNumRegex.sub('PRIVATE', 'I can be reached at p:123-456-7890 or c:234-567-8901')")
print(phoneNumRegex.sub('PRIVATE', 'I can be reached at p:123-456-7890 or c:234-567-8901'))
print("We can also substitute groups using the \group#")
print("i.e. phoneNumReges.sub(r'Area Code: \\1 Local Number: \\2', 'Phone Number: 123-456-7890')")
phoneNumRegex = re.compile(r'\(?(\d{3})\)?[- ](\d{3}-\d{4})')
print(phoneNumRegex.sub(r'Area Code: \1 Local Number: \2', 'Phone Number: 123-456-7890'))
input('Press enter key to continue')
print('\n\n\n')
print('The regex.compile() function can be passed a second argument')
print('''e.g. regex.compile(r'regexToMatch', re.I) is case insensitive
regex.compile(r'regexToMatch', re.DOTALL) means the special character . will match newlines
regex.compile(r'regexToMatch', re.VERBOSE) ignores whitespace and comments for cleaner code
We can pass multiple arguments with the bitwise OR operator '|'
ie. regex.compile(r'regexToMatch', re.VERBOSE | re.DOTALL)''')
