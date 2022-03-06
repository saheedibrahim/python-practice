import math             #imports math module

print ("Printing estimated Square Root of 'a'")     #print statement, heading

def my_sqrt (a):          #function of my_sqrt with parameter 'a'
    x = 1                       #initial variable 'x' is 1
    while True:             #iteration for below expression being True
        y = (x + a/x) / 2.0         #Newton's method for calculating square root
        if y == x:              #boolean, 'y' equals 'x' is True, if not is False
            break                #statement to exit the loop if 'y' equals 'x' is True
        x = y                    #variable 'x' equals variable 'y'
    return x                    #return statement, to return the value of variable 'x'
    
print()                                         #print statement, placeholder
print (my_sqrt(1))                      #print statement, to print estimated square root of 'a'

print ()
print ('Printing 1 through 9:')      #print statement, heading
print ()                                        #print statement, placeholder

def test_sqrt ():            #function of test_sqrt with no parameter
    a = 1                        #initial variable 'a' is 1
    while a <=9:            #iteration for the variable 'a' from 1 to 9
        print ('a =', a,'| my_sqrt (a) =', my_sqrt (a),'| math.sqrt (a) =', math.sqrt (a),'| diff =', abs(math.sqrt (a) - my_sqrt (a)))    #print statement, to print required output
        a = a + 1              #increments 'a' by 1; 'a' is equal to 'a' + 1

test_sqrt()                  #calling function 'test_sqrt'

print ()                                            #print statement, placeholder
print ('Printing 1 through 25:')        #print statement, heading
print()                                             #print statement, placeholder

def test_sqrt ():            #function of test_sqrt with no parameter
    a = 1                        #initial variable 'a' is 1
    while a <=25:          #iteration for the variable 'a' from 1 to 25
        print ('a =', a,'| my_sqrt (a) =', my_sqrt (a),'| math.sqrt (a) =', math.sqrt (a),'| diff =', abs(math.sqrt (a) - my_sqrt (a)))     #print statement, to print required output
        a = a + 1              #increments 'a' by 1; 'a' is equal to 'a' + 1

test_sqrt()                #calling function 'test_sqrt'
