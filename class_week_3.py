# # List [-5,2,5,12]
# def sum_list(list): #define name pass storage
#     sum = 0 # define sum
#     for x in range(len(list)): #function pulling the length of list 
#         sum += list[x] 
#     return sum

# print(sum_list([-5,2,5,12]))

# pie_one = {'name' : 'Apple', 'topping' : 'Ice Cream', 'season_availability' : 'fall'}
# pie_two = {'name' : 'Pecan', 'topping' : 'Whipped Cream', 'season_availability' : 'all'}
# pie_three = {'name' : 'Pumpkin Pie', 'topping' : 'Whipped Creme and Ice Cream', 'season_availability' : 'all'}

# Create a blueprint 
# Constructor 16-21
class Pie:
    def __init__(self, name, topping, season = "All"):
        #Attribute 
        self.name = name 
        self.topping = topping
        self.season = season 

    # Methods 
    def sub_topping(self, topping):
        self.topping = topping 
        return self

    def no_topping(self):
        self.topping = None
        return self

    def change_of_season(self, season):
        self.season = season
        return self

pie_one = Pie("Apple Pie" , "Ice Cream", "Fall")
# pie_one.sub_topping("Chocolate Chip Cookie")
# pie_one.no_topping()
# print(pie_one.topping)
# print(pie_one.name, pie_one.topping)

# pie_one.change_of_season('Winter')
# print(pie_one.season)

# pie_two = Pie("Blueberry", "Chocolate Syrup", "All")
# print(pie_two.name)

# pie_three = Pie("Cherry Pie", "Powdered Sugar")
# print(pie_three.season)
print(pie_one.name, pie_one.topping, pie_one.season)

# chaining
pie_one.change_of_season("winter").sub_topping("chocolate chip")
print(pie_one.season, pie_one.topping)