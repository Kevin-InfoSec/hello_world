def TakeInput(InVal): #Demonstrating a basic function, taking input
    return(input('Please enter your ' + InVal + ' value '))
    
def LoopEx(): #Demontrate for and while loops iterating through themselves
    print('What type of loop would you like to test')
    LoopType = input().lower()
    while LoopType != 'while' and LoopType != 'for':
        LoopType = input('Please enter your loop type (while OR for) ').lower()
    if LoopType == 'for':
        print('How many values in your FOR Loop? You can have 1 to 3 arguments passed to a for loop. Each works slightly differently')
        Val = int(input())
        while Val <1 or Val >3:
              print('Please enter a valid i value')
              Val = int(input())
        if Val == 1:
            print('Your syntax is for i in range(x)')
            print('This will return x times')
            x = int(TakeInput('x'))
            for i in range(x):
                print('i = ' + str(i))
        elif Val == 2:
            print('Your syntax is for i in range(x,y)')
            print('This will return starting at x through y')
            x = int(TakeInput('x'))
            y = int(TakeInput('y'))
            for i in range(x,y):
                print('i = ' + str(i))
        elif Val == 3:
            print('Your syntax is for i in range(x,y,z)')
            print('This will return starting at x through y counting by z')
            x = int(TakeInput('x'))
            y = int(TakeInput('y'))
            z = int(TakeInput('z'))
            for i in range(x,y,z):
                print('i = ' + str(i))
        else:
            print('You broke my input validation!!!')
    elif LoopType == 'while':
        print('Your syntax is while x <comparator> y')
        print('We will also define an iterator')
        print('This will return as long as x <comparator> y is true your iterator will determine how x is modified each step. Please note we will only be evaluating numeric while loops, there are many other ways to use while loops')
        x = int(TakeInput('x'))
        comparator = TakeInput('comparator')
        y = int(TakeInput('y'))
        iterator = int(TakeInput('iterator'))
        while comparator != '==' and comparator != '!=' and comparator != '>' and comparator != '<' and comparator != '>':
            comparator = TakeInput('valid comparator (==,!=,>,<, (we are skipping >= and <=)')
        while iterator <= 0:
            iterator = TakeInput('valid iterator (a number greater than 0)')
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
LoopEx() # You can call this as many times as you like for testing purposes

