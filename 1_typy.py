a = 4 # int - integer
b = 4.5 #float
c = 'Hello world'#str - string
d = True # bool - boolean
e = None # NoneType
f = 4j # complex

vat = 23
net_income = 1000

brutto = net_income*(1+(vat/100))
#print(int(brutto)) rzutowanie
#user_value = float(input('Podaj liczbe: '))


print(c[-1]) #indeksowanie - indexing
print(c[0:5]) # <0:4) slicing
print(c[:5])
print(c[6:])
print(4.0 is 4) #False
print(4.0 == 4) #True
print(bool(c))


# tax_rate = 23
# income = 1000
# tax_value = income*tax_rate/100

# print(tax_value)
# value_brutto = income+tax_value
# print(value_brutto)


# napisz program w ktorym uzytkownik poda imie i rok urodzenia a ty wypiszesz komunikat z jego imieniem oraz wiekiem

# userName = input('Podaj imię:' )
# userYearOfBirth = int(input ('Podaj rok urodzenia:')) #string był
# # print(type(userYearOfBirth))
# userAge = 2026 - userYearOfBirth
# print ('Masz na imię:', userName, 'i masz:', userAge, 'lat')


#rozwin program z liczeniem kwoty brutto, aby vat rate i income byly podawane od uzytkownika

vat_rate = float(input('Podaj stawkę VAT: ')) #string był
income =float (input('Podaj kwotę netto: '))
tax_value = income*vat_rate/100

print('Podatek VAT wynosi:',tax_value, 'zł')
value_brutto = income+tax_value
print('Kwota brutto wynosi: ',value_brutto, 'zł')