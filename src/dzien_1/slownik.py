def liczenie_slow_slownik(zdanie):
    wynik = dict()
    liczrnie = 0 
    x = zdanie.split()
    for i in x:
        if i in wynik:
            wynik[i] += 1
        else:
            wynik.update({i : 1})
    print(wynik)
liczenie_slow_slownik("ala ma kota a kot ma ale")