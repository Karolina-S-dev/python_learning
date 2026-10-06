
# funkcja ktora moze przyjac dowolna ilosc liczb i ma zwrocic ich liste bez powtorzen

def get_list_of_numbers_without_duplicates(*numbers):

    # list_of_numbers = []

    # for number in numbers:
    #     if number not in list_of_numbers:
    #         list_of_numbers.append(number)

    # print(list_of_numbers)

    print(list(set(numbers)))

   

get_list_of_numbers_without_duplicates(10, 20, 30, 40, 10,20)
