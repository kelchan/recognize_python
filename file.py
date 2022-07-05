num1 = 42   #variable declaration, integer
num2 = 2.3      #variable declartion, float
boolean = True      #boolean
string = 'Hello World'      #variable declartion, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']      #list of string
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}      #dictionary
fruit = ('blueberry', 'strawberry', 'banana')       #tuple
print(type(fruit))      #log statement
print(pizza_toppings[1])        #log statement
pizza_toppings.append('Mushrooms')      #dictionary, add value
print(person['name'])       #log statement, list of string
person['name'] = 'George'       #list, string, change value
person['eye_color'] = 'blue'        #list, string, change value
print(fruit[2])         #log statement, list

if num1 > 45:           #if, conditional
    print("It's greater")       #log statement
else:                       #else
    print("It's lower")      #log statement

if len(string) < 5:         #if, conditional
    print("It's a short word!")     #log statement
elif len(string) > 15:      #else if, conditional
    print("It's a long word!")      #log statement
else:                       #else 
    print("Just right!")        #log statement

for x in range(5):          #for loop, conditional  
    print(x)            #log statement
for x in range(2,5):          #for loop, conditional
    print(x)            #log statement
for x in range(2,10,3):     #for loop, conditional 
    print(x)            #log statement
x = 0                   #primitive, assigment
while(x < 5):           #while loop, conditional
    print(x)            #log statement
    x += 1              #primitive, add value

pizza_toppings.pop()    #list, delete value
pizza_toppings.pop(1)   #list, delete value

print(person)           #log statement
person.pop('eye_color')     #dictionary, delete value
print(person)           #log statement 

for topping in pizza_toppings:      #for loop, conditional
    if topping == 'Pepperoni':      #if, conditional
        continue
    print('After 1st if statement')     #log statement
    if topping == 'Olives':         #if, conditional
        break   

def print_hello_ten_times():        #function
    for num in range(10):           #for loop, argument
        print('Hello')              #log statement

print_hello_ten_times()             #function

def print_hello_x_times(x):         #function, parameter
    for num in range(x):            #for loop, arguement
        print('Hello')              #log statement

print_hello_x_times(4)              #function, argument

def print_hello_x_or_ten_times(x = 10):     #function, parameter
    for num in range(x):                    #for loop
        print('Hello')                      #log statement

print_hello_x_or_ten_times()            #function
print_hello_x_or_ten_times(4)           #function, parameter


"""
Bonus section
"""

# print(num3)       
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)