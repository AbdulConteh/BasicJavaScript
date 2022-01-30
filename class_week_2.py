# # List vs Dictionaries 

# person_one = ["Abdul", "Y", "Blue", "True"] 
# print(person_one[2])

# # Dictionary 

# person_two = { 
#     # Key : Value = Key Value Pair 
#     "name" : "Rob", #String 
#     "age" : 24,
#     "food_truck" : True,
#     "items" : ["apple_pie", "pumpkin pie", "peach pie"] # List 
# }

# print(person_two['items'][2])
# print(person_two['age'])
# person_two['loves dogs'] = True
# print(person_two)
# person_two['food_truck'] = False 
# print(person_two)
# person_two['items'][0] = "apple crisp"
# print(person_two)

# person_three = {}
# person_three['name'] = 'Duley'
# print(person_three)

# person_one[0] = 'Sebuh'
# print(person_one)
# Removing values - Pop vs Del 
# value_remove = person_two.pop('age') # Pop returns the value that is deleted 
# print(value_remove)

# del person_two['age'] #delete does not return anything 

#Key of Keys
# print(person_two.keys())

# # Val of Values 
# print(person_two.values())

# # Keys and Values 
# print(person_two.items())

# Conditionals 

# x = 32

# if x > 50:
#     print("Bigger than 50")
    
# elif x > 40:
#     print("Bigger than 40")
# elif x > 30:
#     print("Bigger than 30")
# else:
#     print("Less than 50")

# birds = {
#     "Hygene" : "wack",
#     "Language" : "trash",
#     "Location" : "they do be everywhere"
# }

# for pineapple in birds.keys():
#     print(pineapple)

#     for key, val in birds.items():
#         print(key, val)
#         if key == "Language":
#             print('Bring BUG Spray')
#             #Print(key, val)
#             print(key, " = ", val)

# Functions 
num = 7 

def sum(num):
    # print(num)
    num += 1 
    return num
