from algemene_functies import mijn_functie2

def combinatie(invoer_lijst_2):
        korte_lijst= laag_en_hoog(invoer_lijst_2)
        uitvoer = mijn_functie2(korte_lijst[0], korte_lijst [1])
        return uitvoer

print (combinatie)


print ("\n")

def aanbieding_1(smaak, prijs, korting):
        
        prijsmetkorting = korting * prijs
        nieuwe_prijs = prijs - prijsmetkorting
        
        uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."
        return uitvoer


print (aanbieding_1("aardbei", 4, 0.1))

print ("\n")

def inkomsten_totaal1 (inkomsten, btw):
               
        totaal = 0
        for dagwinst in inkomsten:
                totaal += dagwinst   

        btw_erbij = btw * totaal
        
        uitvoer =f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_erbij} euro btw betaald dient te worden."

        return uitvoer
        
         
zeven_waarden = [220, 430, 125, 160, 205, 90, 345]

print (inkomsten_totaal1(zeven_waarden, 0.09))    

print ("\n")

def inkomsten_totaal8 (inkomsten, btw):
        totaal = 0
        for dagwinst in inkomsten:
                totaal += dagwinst
        return totaal
        
zeven_waarden = [220, 430, 125, 160, 205, 90, 345]

print ("Totaal:")
print (inkomsten_totaal8(zeven_waarden, 0.09))  

print ("\n")


def laag_en_hoog (mijn_lijst):
     laag = min(mijn_lijst)
     Hoog = max(mijn_lijst)
     print (laag)
     print (Hoog)
                 
zeven_waarden = [220, 430, 125, 160, 205, 90, 345]

print(laag_en_hoog(zeven_waarden))

print ("\n")

def gemiddelde (mijn_lijst):
        tel_op = sum(mijn_lijst)
        lengte = len(mijn_lijst)
        uitkomst = tel_op / lengte
        print (uitkomst)

zeven_waarden = [220, 430, 125, 160, 205, 90, 345]
print (gemiddelde(zeven_waarden))

print ("\n")

def gemiddelde10 (mijn_lijst):
        tel_op = sum(mijn_lijst)
        lengte = len(mijn_lijst)
        uitkomst = tel_op / lengte
        print (f"De gemiddelde inkomsten van deze week zijn{uitkomst: .0f} euro.")

zeven_waarden = [220, 430, 125, 160, 205, 90, 345]
print (gemiddelde10(zeven_waarden))

print ("\n")


def meervoudig (invoerlijst):
        
            laag_en_hoog(invoerlijst)
        
             
getallen = [10,5,3,2,1,2,9]

print (meervoudig (getallen))

print ("\n")