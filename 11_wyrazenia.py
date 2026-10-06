# even_numbers = [number for number in range(21) if number % 2 == 0]
# print(even_numbers)
# wyrazenia listy, slownika, zbioru
# generatory (wyrazenie tupli)
# list comprehension, dict comp...

# even_numbers = [
#     number # co jest elementem listy
#     for number in range(21) #źródło - petla for (wymagane)
#     if number % 2 == 0 # warunek - if (opcjonalny)
# ]


# Wyrażenia listy (przedział 1-100):
# 1. stworz liste liczb podzielnych przez dwa i niepodzielnych przez 3
divisible_by_2_and_not_divisible_by_3 = [
    number
    for number in range(1, 101)
    if number % 2 == 0 and number %3 !=0
]

print(divisible_by_2_and_not_divisible_by_3)

# 2. stwórz liste kwadratów liczb podzielnych przez 5

squares_of_numbers_divisible_by_5 = [
    number**2
    for number in range(1, 101)
    if number % 5 == 0
]

print(squares_of_numbers_divisible_by_5)