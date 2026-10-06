# numbers = [1,2,3] #list 
# print(numbers)
# print(type(numbers))

even_numbers = range(0,20,2)
# for number in even_numbers:
#     print(number)

# print(even_numbers)
# print(type(even_numbers))

even_numbers_list = list(even_numbers)
# print(even_numbers_list)
# print(type(even_numbers_list))

# print(15 in even_numbers_list)

even_numbers_list.append(22)
even_numbers_list.insert(-1, 20)

even_numbers_list.remove(10)

deleted_number = even_numbers_list.pop(-1)
print(even_numbers_list)
print(deleted_number)

# sortowac listy (sorted, reverse, .sort(ed))