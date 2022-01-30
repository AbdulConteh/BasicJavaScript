num1 = 42 #variable declaration, primitive number 
num2 = 2.3 #variable declaration, float 
boolean = True #boolean 
string = 'Hello World' #variable declaration , primitive string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration

print(type(fruit)) #log statement 
print(pizza_toppings[1]) #log statement, access value 
pizza_toppings.append('Mushrooms') #dictionary 
print(person['name']) #log statement, access value 
person['name'] = 'George' # list, change value 
person['eye_color'] = 'blue' # list, change value
print(fruit[2]) #log statement, access value

if num1 > 45: # conditionals
    print("It's greater") #log statement 
else: # conditionals
    print("It's lower") #log statement 

if len(string) < 5: # conditionals if 
    print("It's a short word!") #log statement 
elif len(string) > 15: # conditionals else if 
    print("It's a long word!") #log statement 
else: # conditionals else if
    print("Just right!") #log statement 

for x in range(5): # for loop stop
    print(x) #log statement 
for x in range(2,5): # for loop start stop
    print(x) #log statement 
for x in range(2,10,3): # for loop  start stop increments 
    print(x) #log statement 

x = 0 #variable declaration 
while(x < 5): # while loop 
    print(x) #log statement 
    x += 1 #valye change 


pizza_toppings.pop() # list delete value 
pizza_toppings.pop(1) # list delete specific value 

print(person) #log statement 
person.pop('eye_color') # list delete specific value 
print(person) #log statement 

for topping in pizza_toppings: #for loop 
    if topping == 'Pepperoni': #conditional if 
        continue #for loop continue 
    print('After 1st if statement') #log statement 
    if topping == 'Olives': # conditional if 
        break #for loop break 

def print_hello_ten_times(): #function 
    for num in range(10): # for looop 
        print('Hello') #log statement 

print_hello_ten_times() #error

def print_hello_x_times(x): #function 
    for num in range(x): #for loop 
        print('Hello') #log statement 

print_hello_x_times(4) #error

def print_hello_x_or_ten_times(x = 10): #function 
    for num in range(x): #for loop 
        print('Hello') #log statement 

print_hello_x_or_ten_times() #error
print_hello_x_or_ten_times(4) #error


"""
This is 
a multiline
comment
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)