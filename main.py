#arb_args - Takes in any number of arguments and prints them one at a time.
def arb_arg(*arg):
    print(*arg)
 
arb_arg('hi','bye',7,'ha')

#inner_func - Takes in two integers. Two nested functions should perform separate, 
#distinct math operations using the integers.The result of both nested functions should then be added together & printed.
def inner_func(a,b):
    add = a+b
    def plus1(a,b):
        a=a+1
        b=b+1
        c=a+b
        return(c)
    return plus1(a,b) + add
    
print(inner_func(2,4))

#lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings.
#If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name,lunch='Mystery Meat'):
    print(name,lunch)
lunch_lady('wendy')

#sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(a,b):
    return a*b , a+b
print(sum_n_product(2,4))

#alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. 
#Alternatively, you can call a function from inside another function.
#Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_arg = arb_arg

#arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*arg):
    total = 0
    for i in arg:
        total += i 
    return(total/len(arg))
print(arb_mean(5,10,5,20))

#arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*string):
    biggest = 0
    index = 0
    for i in string:
        if len(i) > biggest:
            biggest = len(i)
            index = i
    return index
print(arb_longest_string('hello','bye','longest'))