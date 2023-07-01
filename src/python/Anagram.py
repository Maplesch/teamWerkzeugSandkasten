from collections import Counter

wort1 = input("Bitte geben Sie das 1. Wort ein: ")
wort2 = input("Bitte geben Sie das 2. Wort ein: ")

l1 = len(wort1)
l2 = len(wort2)

if l1 != l2:
    print("Es handelt sich um kein Anagramm")
    
else:
    c1 = Counter(wort1)
    c2 = Counter(wort2)
    
    if c1 == c2:
        print("Es handelt sich um ein Anagramm")
    else:
        print("Es handelt sich um kein Anagramm")
        