
urlaub = 26
alter = int(input("Alter: ", ))
jahre = int(input("Betriebszugehörigkeit:", ))
sbgd = int(input("Schwerbehindertengrad: ", ))

if alter < 18:
    urlaub += 4
else:
    if jahre >= 10:
        urlaub += 2
    if alter > 55:
        urlaub += 2

if sbgd >= 10:
    urlaub += 5


    

print(urlaub)