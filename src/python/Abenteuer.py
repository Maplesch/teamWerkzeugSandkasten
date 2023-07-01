def error():
    print("Entscheide dich für eine der Optionen!")

def ungeheuer():
    print ("Plötzlich gurgelt und wirbelt das Wasser im Becken. Ein riesiger Kopf taucht auf und rülpst.")
    print ("Was machst Du?")
    print ("a Du wirst neugierig und schaust dir das Wesen genauer an")
    print ("b Du gehst in den Kampfmodus, zückst deinem Dolch, welchen du immer bei dir trägst und stürzt dich voller Adrenalin auf dieses Wesen")
    print ("c Du rennst schreiend davon und verkriechst Dich in Deinem Bett")    

def bett():
    print ("Du schläfst den ganzen Tag und lümmelst noch ein wenig auf dem Sofa.")
    end()

def emotion():
    print ("Du spürst, wie dein Gefühl immer stärker wird, wenn du nichts unternimmst, wirst Du platzen")
    print("Was wirst Du tun?")
    print("g Emotion runterschlucken")
    print("h Emotion rauslassen")

def end():
    print("Nach einem langen intensiven Tag gehst du ins Bett und träumst von Chefs, die sich in Ungeheuer verwandeln.")

def kampf():
    print("Das Ungeheuer sieht dich kommen und geht sofort auf Abwehr. Es ist stärker als du und du hast keine Chance. Der Kampf dauert bis zum Abend.")
    print("Schwer verwundet ziehst du dich zurück und versorgst deine Wunden. ")

wahl = "z"
gefuehl = "z"

print ("Es ist schon wieder Montag morgen. Du hast keine Lust auf die langweilige Arbeit, auf deinen Chef, dem du es sowieso nichts recht machen kannst und Deine Kollegen nerven sowieso.")
print ("Was wirst Du tun?")
print ("a krankmachen und das schöne Wetter genießen? - oder")
print ("b dich zur Arbeit quälen, weil du ein pflichtbewusster Mensch bist?")

wahl = input()

while wahl!="a" and wahl!="b":
    error()
    wahl = input()
        

if wahl == "a":

    print ("Die Sonne scheint, wofür entscheidest Du Dich?")
    print ("a du gehst ins Schwimmbad")
    print ("b der Wald ruft dich")
    print ("c du drehst dich nochmal um und schläfst endlich mal richtig aus")
        
    wahl = input()

    while wahl!="a" and wahl!="b" and wahl!="c":
        error()
        wahl = input()

elif wahl =="b":
    print ("Als Du auf der Arbeit erscheinst, ist dein Chef genauso mies drauf wie immer, die Kollegen machen Dienst nach Vorschrift. In Dir keimt ein Gefühl, welches immer stärker zu werden droht. Um welches Gefühl handelt es sich?")
    print ("a Wut/Ärger ")
    print ("b Frustration")
    print ("c Hass")
        
    gefuehl = input()
    wahl = "z"

    while gefuehl!="a" and gefuehl!="b" and gefuehl!="c":
        error()
        gefuehl = input()

if wahl == "a":
    print ("Du chillst ganz entspannt, die Sonne scheint, das Schwimmbad ist noch ziemlich leer. ")
    ungeheuer()
    wahl = input()

    while wahl!="a" and wahl!="b" and wahl!="c":
        error()
        wahl = input()

elif wahl == "b":
    print ("Es ist sehr warm, im schattigen Wald lässt es sich gut aushalten. Du setzt Dich auf eine kleine Lichtung, direkt am Rande eines Sees und chillst ganz entspannt")
    ungeheuer()
    wahl = input()
    while wahl!="a" and wahl!="b" and wahl!="c":
        error()
        wahl = input()

elif wahl == "c":
    bett()
    wahl = input()
    while wahl!="a" and wahl!="b" and wahl!="c":
        error()
        wahl = input()

    while wahl == "c":
        bett()
        wahl = input()

if gefuehl == "a" or gefuehl == "b" or gefuehl =="c":
    emotion()
    wahl = input()

    while wahl!="g" and wahl!="h":
        error()
        wahl = input()

if wahl =="g":
    print ("Du bekommst Magenschmerzen, weil das Gefühl nicht verdaut werden kann. ")
    print ("Schließlich meldest du dich krank und gehst nach Hause und legst dich ins Bett.")
    bett()
    wahl = input()

    while wahl!="a" and wahl!="b" and wahl!="c":
        error()
        wahl = input()

elif wahl == "h" and (gefuehl == "a" or gefuehl =="c"):
    print ("Du wirst von deinen Gefühlen übermannt, nimmst deinen Dolch, den du immer bei dir trägst und willst auf Deinen Chef einstechen. Doch dieser verwandelt sich in ein Ungeheuer und Du hast keine Chance gegen ihn.")
    print ("Du wirst schwer verwundet, stehst unter Schock und gehst nach Hause. Gegen Abend kommst du wieder zur Besinnung.")
    end()

elif wahl == "h" and gefuehl == "b":
    print ("Du fängst an zu schreien, bis Du keine Luft mehr bekommst. Du siehst, wie sich dein Chef in ein Ungeheuer verwandelt und dich angreift. Du zückst deinen Dolch und willst dich wehren, doch du hast keine Chance.")
    print ("Alle starren Dich an und Dir wird nahegelegt, nach Hause zu gehen.")
    print ("Zuhause brauchst Du ein paar Stunden bis Du wieder zur Besinnung kommst.")
    end()

if wahl == "q":
    print ("Deine Neugier ist stärker als die Angst, sprichst das Wesen an: hallo, wer bist Du?")
    print ("es scheint freundlich zu sein und antwortet: Ich bin Nessi und mache hier Urlaub ")
    print ("es entsteht eine rege Unterhaltung und due erfährst eine Menge über das Leben als Seeungeheuer")

    end()

elif wahl == "b":
    kampf()
    end()
