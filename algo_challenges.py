# 1.
# # for i in range(1,256):
# #     print(i)
# 2.
# # ******
# # # n = input()
# # # n = int (n)
# # # sum = 0
# # # for num in range(1,1000,2):
# # #     sum = sum+num
# # #     print(sum)
# # *******
# 3.
# # *********
# # *********

# 4.
# x = 0
# arr = [1,2,5]
# arr_1 = [-5,2,5,12]
# sum = 0

# for i in range(0,len(arr)):
#     sum = sum + arr[i]
# print(sum)

# for i in range(0,len(arr_1)):
#     sum = sum + arr_1[i]
# print(sum)

# # 5.
# arr = [-3, 3, 5, 7]
# max_number = max(arr)
# print(max_number)

# 6.
# def cal_average(num):
#     sum_num = 0 
#     for i in num:
#         sum_num = sum_num + i 

#     avg = sum_num / len(num)
#     return avg

# print(cal_average([1,3,5,7,20]))

# 7.
# start, end = 1, 50
# for num in range(start, end + 1):
#     if num % 2 != 0:
#         print(num, end = " ")

# 8.
# y = 2
# arr = [7,3,6,2,9]
# count = 0
# for i in arr:
#     if i > y:
#         count = count + 1
#         print("The list: " + str(count)) 

# 9.
# arr = [5,15,3,12]
# b = [x**2 for x in arr]
# print(b)

# 10.
# arr = [1,5,-7,4,-3,6,-9]
# print(arr)
# arr = [0 if (x <= 0) else x for x in arr]
# print(arr)

# 11.
# arr = [1,2,3,4,5]
# maximum = max(arr)
# minimum = min(arr)
# print(maximum, minimum)
# sum = len(arr) / sum(arr)
# print(sum)
# past:

# 12.
# def swap_positions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
# list = [1,5,10,-2]
# pos1, pos2 = -2, 1

# print(swap_positions(list, pos1-1, pos2-1))

# 13. ****
# arr = [1, -2, 4, -8, -5]
# def change_values():
#       in arr > 0:
#         print(arr)
#     # elif i in arr < 0:
# #     #     print("Dojo")
# *******

# 14.
# arr = [1,-1,2,-2,-3]

# arr = numpy.char.repalce(arr > -1, "big", arr)
# print(arr)