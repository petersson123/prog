import random

while True:
    svar = input("Vill du spela? (j/n): ")

    if svar == "j":
        t1 = random.randint(1, 6)
        t2 = random.randint(1, 6)
       
        print(f"Tärningskast: {t1}, {t2}")

        if t1 == 6 and t2 == 6:
            print ("sex-vinst")
        elif t1 == t2:
            print("Du vann!")
        elif t2 == t1 + 1 or t1 == t2+1:
            print ("steg-vinst")
        

        else:
            print("Förlust. Försök igen!")

    elif svar == "n":
        print("Hejdå!")
        break  

    else:
        print("Ogiltigt svar. Försök igen.")
