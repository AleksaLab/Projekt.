from random import randint
from klasy import Menu, Gra, Papier
ekwipunek = ["stary_kilof"]
sakwa_na_mineraly = []
wynik = []
kasa = 0

startkasa = randint(0,200)

if startkasa >= 0 and startkasa <= 5:
	kasa += kasa + 9000
	print("Poczatkowe pieniadze: 9000$")
elif startkasa > 5 and startkasa <= 15:
	kasa += kasa + 6000
	print("Poczatkowe pieniadze: 6000$")
elif startkasa > 15 and startkasa <= 30:
	kasa += 4500
	print("Poczatkowe pieniadze 4500$")     
elif startkasa > 30 and startkasa <= 50:
	kasa += 2000
	print("Poczatkowe pieniadze: 2000$")        
elif startkasa > 50 and startkasa <= 80:
	kasa += 1000
	print("Poczatkowe pieniadze: 1000$")
elif startkasa > 80 and startkasa <= 130:
	kasa += 500
	print("Poczatkowe pieniadze: 500$")        
elif startkasa > 130 and startkasa <= 200:
	print("Poczatkowe pieniadze: 0$")

hartowany_zelazny_kilof = 0
stalowy_kilof = 0
tytanowe_wiertlo = 0
stary_kilof = 1
zardzewialy_kilof = 0
super_motyka = 0

rubin = 0
szmaragd = 0
opal = 0
beryl = 0
szafir = 0

p = 0 
ptkU = 0
ptkC = 0

i = 0
st = Menu()
rt = Gra()


while i < 7:
  i += 1
  print("dzien - ", i)
  st.tawerna(kasa,ekwipunek, sakwa_na_mineraly)
  rt.petla(wynik,szmaragd,rubin,szafir,beryl, opal,kasa,sakwa_na_mineraly)
  szmaragd = wynik[0]
  rubin = wynik[1]
  szafir = wynik[2]
  beryl = wynik[3]
  opal = wynik[4]
  kasa = wynik[5]
  wynik = []

  rt.petla(wynik,szmaragd,rubin,szafir,beryl, opal,kasa,sakwa_na_mineraly)
  szmaragd = wynik[0]
  rubin = wynik[1]
  szafir = wynik[2]
  beryl = wynik[3]
  opal = wynik[4]
  kasa = wynik[5]
  wynik = []
  
  if i >= 2:
    if stalowy_kilof >= 1:
      wynik = []
      rt.stalowykilofgra(szmaragd, rubin, szafir, beryl, opal, kasa,sakwa_na_mineraly,wynik)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []
      rt.stalowykilofgra(szmaragd, rubin, szafir, beryl, opal, kasa,sakwa_na_mineraly,wynik)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []
    elif hartowany_zelazny_kilof >= 1:
      wynik = []
      rt.petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]

      wynik = []
      rt.petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []

      rt.petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []

    elif tytanowe_wiertlo >= 1:
      wynik = []
      rt.petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []
      rt.petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []
      rt.petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []
      rt.petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      kasa = wynik[5]
      wynik = []
    elif super_motyka >= 1:
      rt.super_motyka_gra(szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly, wynik)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      
      wynik = []
      rt.super_motyka_gra(szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly, wynik)
      szmaragd = wynik[0]
      rubin = wynik[1]
      szafir = wynik[2]
      beryl = wynik[3]
      opal = wynik[4]
      
      wynik = []
  
  rt.sprzedaz(szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly, wynik)
  szmaragd = wynik[0]
  rubin = wynik[1]
  szafir = wynik[2]
  beryl = wynik[3]
  opal = wynik[4]
  kasa = wynik[5]
  
  wynik = []
  rt.sklep(kasa, stary_kilof, stalowy_kilof, hartowany_zelazny_kilof, tytanowe_wiertlo, ekwipunek, wynik,super_motyka)
  kasa = wynik[0]
  stary_kilof = wynik[1]
  stalowy_kilof = wynik[2]
  hartowany_zelazny_kilof = wynik[3]
  tytanowe_wiertlo = wynik[4]
  super_motyka = wynik[5]
  Papier.pkn(p,ptkU, ptkC)
  print("TWOJE STATYSTYKI PO TYM DNIU:")
  print("TWOJ EKWIPUNEK:", ekwipunek)
  print("TWOJE PIENIADZE:", kasa)
  print("TWOJE MINERALY:", sakwa_na_mineraly)

  wynik = []

if kasa >= 25000:
	print("WYGRALES ZDOBYWAJAC OKRESLONA PULE PIENIEDZY, TWOJE PIENIADZE TO:", kasa)
elif kasa < 25000:
	print("NIE WYGRYWASZ, BO NIE OSIAGNALES OKRESLONEJ PULI PIENIEDZY, TWOJE PIENIADZE TO:", kasa)