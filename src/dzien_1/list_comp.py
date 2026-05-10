lista = [1,2,3 ,4 ,5 ,6, 7 ,8 ,9 , 10]
# lista2 = [n for n in lista]
# print(lista2)
# lista2 = [n*n for n in lista]
# print(lista2)
# lista2 = [n for n in lista if n%2 == 0 ]
# 3rint(lista2)
# lista2 = [(m,n) for n in "abcd"  for m in range(4)]
# print(lista2)
imiona = ["Olek", "Daniel", "Euredyka"]
przydomki = ["Cwel", "Sigma", "Szmata"]
# #razem = dict(zip(imiona,przydomki))
# slownik = {imie.lower() : przydomek.upper() for imie , przydomek in zip(imiona, przydomki)}
# print(slownik)
# liczby = [1, 1 ,2 ,2 ,3,4,5,6,7,6,7,8,5,4]
# nums = set(liczby)
# print(nums)
# list2 = [n*n for n in lista if n%2 == 1]
# print(list2)
imiona = ["Olek", "Daniel", "Euredyka", "Sigma", "Chad"]
wyniki = [45, 72, 38, 91, 60]
odpowiedz = [imie.upper() for imie, wynik in zip(imiona,wyniki) if wynik > 50]
print(odpowiedz)