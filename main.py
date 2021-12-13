'''
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''

gép = 3
szam = int(input('Kérek egy számot! '))
if gép < szam :
  print('A gondolt szám kissebb! ')
elif gép > szam : 
  print('A gondolt szám nagyobb! ')
else:
  print('A megadott szám egyenlő! ')
  