# Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ]
# students = [
#     {'first_name':  'Michael',
#     'last_name' : 'Jordan'
#     },
#     {'first_name' : 'John',
#     'last_name' : 'Rosales'
#     }
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10,'y': 20} ]

# x[1][0] = 15 
# print(x)

# students[0]['last_name'] = 'Bryant'
# print(students)

# sports_directory['soccer'] [0] = 'Andres'
# print(sports_directory)

# z[0]['y'] = 30
# print(z)

# Iterate through a List of Dictionaries
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def iterateDictionary(some_list):
#     for value in some_list:
#         print(value['first_name'], value['last_name']) 

# iterateDictionary(students)

# Get Values fFrom a List of Dictionaries 

# students2 = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def iterateDictionary2(key_name, some_list):
#     for value in some_list:
#         print(value[key_name])

# iterateDictionary2('last_name', students2)
# iterateDictionary2('first_name', students2)

# Iterate Through a Dictionary with List Values 

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for value in dojo:
#         print(len(dojo[value])) 
#         print(dojo[value][0])
#         for keys in dojo: 
#             print(dojo[keys])
# printInfo(dojo)
