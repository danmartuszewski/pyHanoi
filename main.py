#!/usr/bin/python
#-*- coding: utf-8 -*-

import hanoi

q = hanoi.hanoi()

print q.__doc__

ile = input('Ilość krążków: ')

q.ustaw(ile)

while not q.sprawdz() :
    try:
        q.pokaz();
        try:
            s = input('Skad: ')
            d = input('Dokad: ')
            paliki = ['A', 'B', 'C']
            if s != d and (1<=s<=3 and 1<=d<=3):
                print '+----------------------------------+'
                print '|\t Ruch: ' + str(q.iRuchow + 1)
                print '|\t ' + paliki[s-1] + ' => ' + paliki[d-1]
                print '|\t ' + str(s) + ' => ' + str(d)
                print '+----------------------------------+'
                r = q.przesun(s,d)
                if  r == 2:
                    print '+----------------------------------+'
                    print '|' + 'Przypomnij sobie zasady!'.center(36)
                    print '+----------------------------------+'
                elif r == 3:
                    print '+----------------------------------+'
                    print '|' + 'Palik jest pusty!'.center(36)
                    print '+----------------------------------+'
            else:
                print '+----------------------------------+'
                print '|' + 'Brak ruchu'.center(36)
                print '+----------------------------------+'
        except NameError:
            print '+----------------------------------+'
            print '|' + 'Używaj cyfr 1, 2 lub 3'.center(36)
            print '+----------------------------------+'
    except SyntaxError:
        pass


q.pokaz()
print '+-----------KONIEC-GRY-------------+'
print '|\t Ilość ruchów: ' + str(q.iRuchow);
print '+----------------------------------+'
print 'Copyright Daniel Martuszewski'.rjust(36)

