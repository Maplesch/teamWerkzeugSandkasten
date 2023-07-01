wort = input("Geben Sie eine Zeichenkette ein: ")

# def zeichen_vergleich(a, b):
#     print("hallo")
#    
#     if wort[a] == wort[b]:
#         a += 1
#     else:
#         "Die Zeichenkette ist kein Palindrom!"
#         return

laenge = len(wort)

i = 0
j = int(laenge-1)
k = "yes"

while i < laenge/2:
#    print(wort[i])
#    print(wort[j])
    if wort[i] == wort[j]:
        i += 1
        j -= 1
    else:
        print("Das Wort ist kein Pallindrom")
        k = "no"
        break
    
if k == "yes":
    print("Das Wort ist ein Pallindrom")
