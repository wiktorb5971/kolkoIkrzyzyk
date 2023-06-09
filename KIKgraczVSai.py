#Autorzy Wiktor Balasa && Kamil Kądzielawa wersja: 1.0 gracz vs ai (gracz zawsze wygrywa bo jestesmy lepsi niz jakies tam AI)
import random

def drukuj_plansze(plansza):
    print('-------------')
    print('| ' + plansza[0] + ' | ' + plansza[1] + ' | ' + plansza[2] + ' |')
    print('-------------')
    print('| ' + plansza[3] + ' | ' + plansza[4] + ' | ' + plansza[5] + ' |')
    print('-------------')
    print('| ' + plansza[6] + ' | ' + plansza[7] + ' | ' + plansza[8] + ' |')
    print('-------------')

def sprawdz_wygrana(plansza):
    warunki_wygranej = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # wygrane poziome
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # wygrane pionowe
        [0, 4, 8], [2, 4, 6]  # wygrane przekątne
    ]

    for warunek in warunki_wygranej:
        if plansza[warunek[0]] == plansza[warunek[1]] == plansza[warunek[2]] != ' ':
            return True
    return False

def ruch_gracza(plansza, gracz):
    ruch = int(input("Gracz " + gracz + ", wykonaj ruch (0-8): "))
    if plansza[ruch] == ' ':
        plansza[ruch] = gracz
    else:
        print("To miejsce jest już zajęte!")
        ruch_gracza(plansza, gracz)

def ruch_AI(plansza, gracz):
    dostepne_ruchy = [i for i, x in enumerate(plansza) if x == ' ']
    ruch = random.choice(dostepne_ruchy)
    plansza[ruch] = gracz

def kolko_i_krzyzyk():
    plansza = [' '] * 9
    gracz = 'X'

    while True:
        drukuj_plansze(plansza)

        if gracz == 'X':
            ruch_gracza(plansza, gracz)
        else:
            ruch_AI(plansza, gracz)

        if sprawdz_wygrana(plansza):
            drukuj_plansze(plansza)
            if gracz == 'X':
                print("Gracz X wygrywa!")
            else:
                print("Gracz O wygrywa!")
            break
        elif ' ' not in plansza:
            drukuj_plansze(plansza)
            print("Remis!")
            break

        if gracz == 'X':
            gracz = 'O'
        else:
            gracz = 'X'

kolko_i_krzyzyk()
