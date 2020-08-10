#!/usr/bin/env python3
def TakeInput(InVal): #Demonstrating a basic function, taking input
    return(input('Please enter your ' + InVal + ' value '))
    
def LoopEx(): #Demontrate for and while loops iterating through themselves
    print('What type of loop would you like to test')
    LoopType = input().lower()
    while LoopType != 'while' and LoopType != 'for':
        LoopType = input('Please enter your loop type (while OR for) ').lower()
    test = 'failure'
    if LoopType == 'for':
        print('How many values in your FOR Loop? You can have 1 to 3 arguments passed to a for loop. Each works slightly differently')
        Val = input()
        while Val !='1' and Val !='2' and Val !='3':
            Val = input('Please enter a valid i value (1,2, or 3) ')
        Val = int(Val)
        if Val == 1:
            print('Your syntax is for i in range(x)')
            print('This will return x times (starting at 0)')
            x = -1
            while test == 'failure':
                try:
                    x = int(TakeInput('valid positive integer for x'))
                    if x >= 1:
                        test = 'success'
                except:
                    continue
            for i in range(x):
                print('i = ' + str(i))
        elif Val == 2:
            print('Your syntax is for i in range(x,y)')
            print('This will return starting at x through y (x must be less than y)')
            while test == 'failure':
                try:
                    x = int(TakeInput('valid integer for x'))
                    y = int(TakeInput('valid integer for y'))
                    if x >= y:
                        print('x must be less than y')
                    else:
                        test = 'success'
                except:
                    continue
            for i in range(x,y):
                print('i = ' + str(i))
        elif Val == 3:
            print('Your syntax is for i in range(x,y,z)')
            print('This will return starting at x through y counting by z')
            while test == 'failure':
                try:
                    x = int(TakeInput('valid integer for x'))
                    y = int(TakeInput('valid integer for y'))
                    z = int(TakeInput('valid integer for z'))
                    if z == 0:
                        print('A zero iterator will cause an infinite loop!')
                    elif x >= y and z > 0:
                        print('x must be less than y with a positive iterator')
                    elif x <= y and z < 0:
                        print('x must be greater than y with a negative iterator')
                    else:
                        test = 'success'
                except:
                    continue
            for i in range(x,y,z):
                print('i = ' + str(i))
        else:
            print('You broke my input validation!!!')
    elif LoopType == 'while':
        print('Your syntax is while x <comparator> y')
        print('We will also define an iterator')
        print('This will return as long as x <comparator> y is true your iterator will determine how x is modified each step. Please note we will only be evaluating numeric while loops, there are many other ways to use while loops')
        while test == 'failure':
            try:
                x = int(TakeInput('valid integer x'))
                test = 'success'
            except:
                continue
        comparator = TakeInput('comparator')
        test2 = 'failure'
        while test2 == 'failure':
            try:
                y = int(TakeInput('valid integer y'))
                test2 = 'success'
            except:
                continue
        test3 = 'failure'
        while test3 == 'failure':
            try:
                iterator = int(TakeInput('valid positive integer iterator'))
                if iterator > 0:
                    test3 = 'success'
            except:
                continue
        while comparator != '==' and comparator != '!=' and comparator != '>' and comparator != '<' and comparator != '>':
            comparator = TakeInput('valid comparator (==,!=,>,<, (we are skipping >= and <=)')
        if comparator == '==':
            if x == y:
                while x == y:
                    print('Your syntax is as long as x = y, change x by iterator each loop')
                    print(str(x) + ' is still equal to ' + str(y))
                    x += iterator
            else:
                print('x does not equal y so your loop will never run!')
        elif comparator == '!=':
            if x == y:
                print('x ' + str(x) + ' is equal to y ' + str(y) + ', your loop will never run!')
            while x != y:
                print('Your syntax is as long as x is not equal to y, add iterator to x each loop')
                print('x ' + str(x) + ' is not equal to y ' + str(y))
                if x > y:
                    print('You made an infinte loop! x will never equal y')
                    break
                x += iterator
        elif comparator == '>':
            while x > y:
                print('Your syntax is as long as x is greater than y, subtract iterator from x each loop')
                print('Your x ' + str(x) + ' is greater than y ' + str(y))
                x -= iterator
        elif comparator == '<':
            while x < y:
                print('Your syntax is as long as x is less than y, add iterator to x each loop')
                print('You x ' + str(x) + ' is less than y ' + str(y))
                x+= iterator
        else:
            print('You broke my program! ' + comparator + ' is not a valid comparator!')
    else:
        print('How did you break my input validation?')

if __name__ == '__main__':
    LoopEx() # You can call this as many times as you like for testing purposes

