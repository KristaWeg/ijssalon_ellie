def mijn_functie_1(para1, para2, para3, para4):
   getal_1 = para1 **2
   getal_2 = para2 **2
   getal_3 = para3 **2
   getal_4 = para4 **2
   return getal_1, getal_2, getal_3, getal_4
   
totaal = mijn_functie_1 (2,4,10,12)

print (totaal)

def mijn_functie3 (*para8):
   for getal in para8:
      print(getal**2)

intotaal = mijn_functie3(2,4,10,12)

print (intotaal)


def mijn_functie2 (a,b):
   optellen= a + b
   aftrekken= a  - b
   keer= a * b
   delen= a / b
   return optellen, aftrekken, keer, delen

print (mijn_functie2(12,3))
print (mijn_functie2(12,2))
print (mijn_functie2(10,5))
print (mijn_functie2(100,20))

