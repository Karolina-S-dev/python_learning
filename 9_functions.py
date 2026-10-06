# 1. napisz program w którym stworzysz słownik z listy liczb: [1,2,3,4,5], gdzie klucz to liczby od 1 do 5 a wartosci to ich potegi

# def get_powers_of_numbers(*numbers_list):

#     numbers_power = []
#     for number in numbers_list:
#         numbers_power.append(number**2)
#     print(numbers_power)
#     numbers_dict = dict(zip(numbers_list, numbers_power))
#     print(numbers_dict)

# get_powers_of_numbers(1, 2, 3, 4, 5)


# numbers=[1,2,3,4,5]
# slownik={}

# for number in numbers:
#     slownik[number]=number**2


# 2. popros uzytkownika o podanie 5 imion, natsepnie zapytaj od kotrego do ktorego imienia chce zobaczyc i wypisz te imiona

# def show_names():
#     print('Podasz mi teraz 5 imion')
#     names_list = []

#     for i in range(5):
#         name = input(f"Podaj {i+1} imię: ")
#         names_list.append(name)
#         print(names_list)

#     from_which_name = int(input('Od którego imienia chcesz zobaczyć?'))-1
#     to_which_name = int(input('Do którego imienia chcesz zobaczyć?'))
#     print(names_list[from_which_name:to_which_name])

# show_names()


# 3. napisz funckje ktora obliczy srednia przeslanych ocen (ilość ocen może być różna)

# def get_average_of_grades(*grades):
#     sum_of_grades = sum(grades)
#     length_of_grades = len(grades)
#     average_of_grades = sum_of_grades/length_of_grades
#     print(average_of_grades)

# get_average_of_grades(4.75, 5, 3.2)


# 4. Zadanie - GRA W SKRZYNKI. Napisz krótką grę w której masz 3 ruchy za każdym razem masz szansę spotkać po drodze SKARB lub NIC (Ustaw, że jest 30% szansy, że nie spotkasz niczego. 70%, że będzie skarb).

#     Skrzynki mają różne kolory.
#     Kolor skarbu oznacza jak rzadka jest ta skrzynka
#     szara - 60%
#     niebieska - 25%
#     fioletowa - 10%
#     platynowa - 5%

#     Ustaw złoto jako to co może "wypaść" ze skarbu:
#     szara - 1000,
#     niebieska - 3000,
#     fioletowy - 6000,
#     platynowa - 10000

#     Wypisuj po kazdym ruchu oraz na koniec gry ilosc zebranego dotychczas złota.

#     Podpowiedź: polecam funkcje choices z modułu random.

# import random

# gold = 0

# for i in range(3):
#     chances = ['treasure', 'nothing']
#     what_you_met = random.choices(chances, weights=[0.7, 0.3])
#     print(what_you_met)

#     if what_you_met == ['treasure']:
#         boxes = ['szara', 'niebieska', 'fioletowa', 'platynowa']
#         what_box_you_met = random.choices(
#             boxes, weights=[0.6, 0.25, 0.1, 0.05])
#         print(what_box_you_met)

#         if what_box_you_met == ['szara']:
#             gold += 1000
#         elif what_box_you_met == ['niebieska']:
#             gold += 3000
#         elif what_box_you_met == ['fioletowa']:
#             gold += 6000
#         elif what_box_you_met == ['platynowa']:
#             gold += 10000

#     print(f"Do tej pory zebrałeś {gold} złota")

# print(f"Koniec gry! Zebrałeś {gold} złota")


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# KINO
# Stworz dwa slowniki: z trzema filmami i cenami i trzema przekaskami i cenami, popros o podanie imienia nastepnie powitaj w kinie. 1 wybranie filmu 2 wybranie
# przekaski 3 podanie ceny do zaplaty i zyczenia milego filmu

def get_price(items, user_choice):
    dictionary_position_in_list = items[user_choice-1]
    for value in dictionary_position_in_list.values():
        price = value
    return price


movies = [
    {"Top Gun: Maverick": 50},
    {"Kevin sam w domu": 40},
    {"Harry Potter i Insygnia Śmierci II": 35}
]

snacks = [
    {"nachos": 15},
    {"popcorn": 10},
    {"gummy": 8}
]

to_pay = 0

client_name = input("Podaj proszę swoje imię: ")
print(f"Witaj w kinie {client_name} !")

# movie choice and price calculation
movie_choice = int(input(
    "Wybierz film: 1. Top Gun: Maverick, 2. Kevin sam w domu, 3. Harry Potter i Insygnia Śmierci II: "))
result_movie = get_price(movies, movie_choice)
to_pay += result_movie

# snacks choice and price calculation
snacks_choice = int(input(
    "Wybierz przekąskę: 1. Nachos, 2. Popcorn, 3. Gummy: "))
result_snacks = get_price(snacks, snacks_choice)
to_pay += result_snacks

# total amount
print(f"Łącznie do zapłaty masz: {to_pay} zł. Miłego filmu!")


# cw uzytkownik wpisze liczby, napisz dwie funkcje, jedna przemnaza wszystko razy dwa, a druga zwraca tylko parzyste, zapytaj uzytkownika z ktorej chce skorzystac i taka zastosuj

# def get_numbers_multiplied_by_2(numbers):
#     numbers_multiplied_by_2 = []
#     for number in numbers:
#         numbers_multiplied_by_2.append(number*2)
#     return numbers_multiplied_by_2


# def get_even_numbers(numbers):
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbers


# ustalic separator
# separator = ','
# all_numbers = input('Podaj liczby (rozdziel przecinkiem): ')

# numbers = [int(number) for number in all_numbers.split(separator)]
# print(numbers)
# numbers = all_numbers.split(separator)


# user_numbers = []
# while True:
#     user_number = input("Wpisz liczbę. Aby skończyć wpisz q: ")
#     if user_number == 'q':
#         break
#     else:
#         user_numbers.append(int(user_number))

# print(type(user_numbers))
# print(user_numbers)
# user_question = int(input(
#     "Wybierz: 1. Mnożenie liczb razy 2, 2. Liczby parzyste: "))

# if user_question ==1:
#     #przypisanie definicji funkcji do zmiennej
#     function = get_numbers_multiplied_by_2
# elif user_question == 2:
#     function = get_even_numbers

# result = function(user_numbers)
# print(f'Wynik: {result}')
# if user_question == 1:
#     get_numbers_multiplied_by_2(user_numbers)
#     result = get_numbers_multiplied_by_2(user_numbers)
#     print(f"{user_numbers} pomnożone razy 2 to: {result}")

# elif user_question == 2:
#     get_even_numbers(user_numbers)
#     result_even = get_even_numbers(user_numbers)
#     print(f"Wśród {user_numbers} liczby parzyste to: {result_even}")


# Napisz grę ze zgadywaniem liczby. Losujesz liczbe do zgadniecia, pytasz uzytkownika o liczbe tak dlugo az nie zgadnie. Po każdym zgadnieciu podpowiadaj: więcej/mniej

# import random
# numbers = range(0, 101)
# # for number in numbers:
# #  print(number)
# draw_result = random.choice(numbers)
# print(f"Wylosowana liczba to: {draw_result}")

# while True:
#     user_guessing = int(input("Zgadnij liczbę (1-100): "))

#     if user_guessing > draw_result:
#         print("Mniej")
#     elif user_guessing < draw_result:
#         print("Więcej")
#     else:
#         print("Gratulacje, zgadłeś!")
#         break
