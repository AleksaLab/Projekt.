from random import randint
import time
class Menu:
  
  
  @staticmethod
  def tawerna(kasa,ekwipunek, sakwa_na_mineraly):
    dzien1 = None
    while dzien1 != "Q":
        dzien1 = input("E - ekwipunek, K - kasa, M = sakwa_na_mineraly, R - start kopania | ")
        if dzien1 == "E" or dzien1 == "e":
            print(ekwipunek)
        elif dzien1 == "K" or dzien1 == "k":
            print(kasa)
        elif dzien1 == "M" or dzien1 == "m":
            print(sakwa_na_mineraly)
        elif dzien1 == "R" or dzien1 == "r":
            print("Zaczynanie nowego dnia!")
            break 
class Gra:
  @staticmethod
  def petla(wynik, szmaragd, rubin, szafir, beryl, opal, kasa,sakwa_na_mineraly):
    dzien1kopanie = randint(0,500)
    
    if dzien1kopanie >= 0 and dzien1kopanie <= 5:               #5
      print("\n##############################")
      print("##### WYDOBYTO MINERAL! ######")
      print("#### ZDOBYWASZ SZMARAGD #####")
      print("##############################")
      szmaragd = szmaragd + 1
      sakwa_na_mineraly.append("szmaragd")
    elif dzien1kopanie >= 6 and dzien1kopanie <= 30:            
      print("\n################################")                   #24
      print("### GUBISZ CZESC PIENIEDZY! ####")
      print("########  TRACISZ 3000$ ########")
      print("################################")
      kasa = kasa - 3000 
    elif dzien1kopanie >= 31 and dzien1kopanie <= 45:
      print("\n##############################")                   #14
      print("##### WYDOBYTO MINERAL!  #####")
      print("###### ZDOBYWASZ RUBIN  ######")
      print("##############################")
      rubin = rubin + 1
      sakwa_na_mineraly.append("rubin")
    elif dzien1kopanie >= 46 and dzien1kopanie <= 70:
      print("\n##################################")
      print("#### GUBISZ CZESC PIENIEDZY! #####")                    #24    
      print("######     TRACISZ 4000$    ######")
      print("##################################")
      kasa = kasa - 4000
    elif dzien1kopanie >= 71 and dzien1kopanie <= 90:
      print("\n##############################")                    #19
      print("##### WYDOBYTO MINERAL! ######")
      print("###### ZDOBYWASZ SZAFIR  ######")
      print("##############################")
      szafir = szafir + 1
      sakwa_na_mineraly.append("szafir")  
    elif dzien1kopanie >= 91 and dzien1kopanie <= 150:              
        print("\n###################################")              #59
        print("##### GUBISZ CZESC PIENIEDZY! #####")
        print("######      TRACISZ 1000$   ########")
        print("###################################")
        kasa = kasa - 1000
    elif dzien1kopanie >= 151 and dzien1kopanie <= 159:
        print("\n##############################")               #8
        print("##### WYDOBYTO MINERAL! ######")
        print("####  ZDOBYWASZ OPAL #######")
        print("##############################")
        opal = opal + 1
        sakwa_na_mineraly.append("opal")
    elif dzien1kopanie >= 160 and dzien1kopanie <= 230:
        print("\n###################################")                 #70
        print("##### GUBISZ CZESC PIENIEDZY! #####")
        print("######    TRACISZ 500$   ##########")       
        print("###################################")
        kasa = kasa - 500
    elif dzien1kopanie >= 230 and dzien1kopanie <= 249:
        print("\n##############################")               #19
        print("##### WYDOBYTO MINERAL! ######")
        print("####  ZDOBYWASZ BERYL ########")
        print("##############################")
        beryl = beryl + 1
        sakwa_na_mineraly.append("beryl")
    elif dzien1kopanie >= 250 and dzien1kopanie <=500:
        print("\n#################################")
        print("#####   NIC NIE WYDOBYWASZ! #####")
        print("#################################")
    wynik.append(szmaragd)
    wynik.append(rubin)
    wynik.append(szafir)
    wynik.append(beryl)
    wynik.append(opal)
    wynik.append(kasa)
  
  
  @staticmethod
  def sprzedaz(szmaragd, rubin, szafir, beryl, opal, kasa, sakwa_na_mineraly, wynik):
  	while True:
  		print("\nKtore mineraly chcesz sprzedac?")
  		print("SZMARAGD (5000$ za brylke) - Sm")
  		print("OPAL (4500$ za brylke) - O")
  		print("RUBIN (3500$ za brylke) - R")
  		print("SZAFIR (2000$ za brylke) - Sz")
  		print("BERYL (2000$ za brylke) - Be")
  		print("Kliknij C by przejsc dalej")
  		mineralinp = input()
  		if mineralinp == "Sm" or mineralinp == "sm" and szmaragd >= 1:
  			kasa += 5000
  			sakwa_na_mineraly.remove("szmaragd")
  			szmaragd = szmaragd - 1
  			print("\nSprzedales szmaragd!")
  			print("Saldo:", kasa) 
  		elif mineralinp == "R" or mineralinp == "r" and rubin >= 1:
  			kasa += 3500
  			sakwa_na_mineraly.remove("rubin")
  			rubin = rubin - 1
  			print("\nSprzedales rubin!")
  			print("Saldo:", kasa) 
  		elif mineralinp == "Sz" or mineralinp == "sz" and szafir >= 1:
  			kasa += 2000
  			sakwa_na_mineraly.remove("szafir")
  			szafir = szafir - 1
  			print("\nSprzedales szafir!")
  			print("Saldo:", kasa)
  		elif mineralinp == "O" or mineralinp == "o" and opal >= 1:
  			sakwa_na_mineraly.remove("opal")
  			kasa += 4500
  			opal = opal - 1
  			print("\nSprzedales opal!")
  			print("Saldo:", kasa)
  		elif mineralinp == "Be" or mineralinp == "be" and beryl >= 1:
  			sakwa_na_mineraly.remove("beryl")
  			kasa += 2000
  			beryl = beryl - 1
  			print("\nSprzedales beryl!")
  			print("Saldo:", kasa)
  		elif mineralinp == "C" or mineralinp == "c":
  			break
  		else:
  			print("\nNie mozesz sprzedac mineralu, ktorego nie masz!")
  	wynik.append(szmaragd)
  	wynik.append(rubin)
  	wynik.append(szafir)
  	wynik.append(beryl)
  	wynik.append(opal)
  	wynik.append(kasa)
    

  @staticmethod
  def sklep(kasa, stary_kilof, stalowy_kilof, hartowany_zelazny_kilof, tytanowe_wiertlo,ekwipunek,wynik,super_motyka):
    while True:
      print("\nCENNIK:")
      print("\nStalowy Kilof (Zwieksza szczescie wydobycia mineralow i losowe wydarzenie o 1) - 2000$, klinkij S by kupic")
      print("\nHartowany Zelazny Kilof (Zwieksza ilosc losowego wydarzenia o 2) - 3000$, klinkij H by kupic")
      print("\nSuper Motyka Zwiększa szanse wydobycia minerału) - 8000$, kliknij Sh by kupić")
      print("\nTytanowe Wiertlo (Zwieksza ilosc losowego wydarzenia o 4 i szczescie wydobycia mineralow - 6000$, klinkij T by kupic")
      print("\nKliknij C by zakonczyc dzien")
      sklepin = input()
      if sklepin == "S" or sklepin == "s" and kasa >= 2000:
        kasa = kasa - 2000
        ekwipunek.append("stalowy_kilof")
        stary_kilof =  0
        hartowany_zelazny_kilof =  0
        tytanowe_wiertlo =  0
        stalowy_kilof = stalowy_kilof + 1
        print("Zakupiono stalowy kilof!")
      elif sklepin == "H" or sklepin == "h" and kasa >= 3000:
        kasa = kasa - 3000
        ekwipunek.append("hartowany_zelazny_kilof")
        hartowany_zelazny_kilof = hartowany_zelazny_kilof + 1
        stalowy_kilof =  0
        stary_kilof =  0
        tytanowe_wiertlo =  0
        print("Zakupiono hartowany zelazny kilof!")

      elif sklepin == "Sh" or sklepin == "sh" and kasa >= 8000:
        kasa -= 8000
        ekwipunek.append("super_motyka")
        hartowany_zelazny_kilof = 0
        stalowy_kilof = 0
        super_motyka += 1
        stalowy_kilof = 0
        tytanowe_wiertlo = 0
        print("Zakupiono super motyke!")
      elif sklepin == "T" or sklepin == "t" and kasa >= 6000:
        kasa = kasa - 6000
        ekwipunek.append("tytanowe_wiertlo")
        tytanowe_wiertlo = tytanowe_wiertlo + 1
        stalowy_kilof = 0
        stary_kilof = 0
        hartowany_zelazny_kilof = 0
        print("Zakupiono tytanowe wiertlo")
      elif sklepin == "C" or sklepin == "c":
        break
      else:
        print("\nNie stac cie na ten przedmiot lub wybrales zly przycisk!")
    wynik.append(kasa)
    wynik.append(stary_kilof)
    wynik.append(stalowy_kilof)
    wynik.append(hartowany_zelazny_kilof)
    wynik.append(tytanowe_wiertlo)
    wynik.append(super_motyka)
    

  @staticmethod
  def stalowykilofgra(szmaragd, rubin, szafir, beryl, opal, kasa,sakwa_na_mineraly,wynik):
  	dzien1kopanie = randint(0,320)
  	
  	if dzien1kopanie >= 0 and dzien1kopanie <= 10:               #10
  		print("\n##############################")
  		print("##### WYDOBYTO MINERAŁ! ######")
  		print("#### ZDOBYWASZ SZMARAGD #####")
  		print("##############################")
  		szmaragd = szmaragd + 1
  		sakwa_na_mineraly.append("szmaragd")
  	elif dzien1kopanie >= 11 and dzien1kopanie <=23 :    #12
  		print("\n################################")
  		print("### GUBISZ CZESC PIENIEDZY! ####")
  		print("########  TRACISZ 3000$ ########")
  		print("################################")
  		kasa -= 3000   
  	elif dzien1kopanie >= 23 and dzien1kopanie <= 43:
  		print("\n##############################")                   #20
  		print("##### WYDOBYTO MINERAŁ!  #####")
  		print("###### ZDOBYWASZ RUBIN  ######")
  		print("##############################")
  		rubin = rubin + 1
  		sakwa_na_mineraly.append("rubin")   
  	elif dzien1kopanie >= 44 and dzien1kopanie <= 56:
  		print("\n################################")                  #12
  		print("### GUBISZ CZESC PIENIEDZY! ####")
  		print("########  TRACISZ 4000$ ########")
  		print("################################")
  		kasa -= 4000  
  	elif dzien1kopanie >= 57 and dzien1kopanie <= 97:
  		print("\n##############################")                    #40
  		print("##### WYDOBYTO MINERAŁ! ######")
  		print("####  ZDOBYWASZ SZAFIR ######")
  		print("##############################")
  		szafir = szafir + 1
  		sakwa_na_mineraly.append("szafir")  
  	elif dzien1kopanie >= 98 and dzien1kopanie <= 128:
  		print("\n###################################")                 
  		print("##### GUBISZ CZESC PIENIEDZY! #####")                  #30
  		print("######      TRACISZ 1000$   ########")
  		print("###################################")
  		kasa -= 1000    
  	elif dzien1kopanie >= 129 and dzien1kopanie <= 150:
  		print("\n##############################")               #21
  		print("##### WYDOBYTO MINERAŁ! ######")
  		print("####  ZDOBYWASZ OPAL #######")
  		print("##############################")
  		szafir = szafir + 1
  		sakwa_na_mineraly.append("szafir")
  	elif dzien1kopanie >= 151 and dzien1kopanie <= 186:
  		print("\n###################################")                 
  		print("##### GUBISZ CZESC PIENIEDZY! #####")                  #35
  		print("######      TRACISZ 500$   ########")
  		print("###################################")
  		kasa -= 500
  	elif dzien1kopanie >= 187 and dzien1kopanie <= 227:
  		print("\n##############################")                   #40
  		print("##### WYDOBYTO MINERAŁ!  #####")
  		print("###### ZDOBYWASZ BERYL  ######")
  		print("##############################")
  		beryl = beryl + 1
  		sakwa_na_mineraly.append("beryl")
  	elif dzien1kopanie >= 228 and dzien1kopanie <= 320:
  		print("\n#################################")                
  		print("#####   NIC NIE WYDOBYWASZ! #####")                
  		print("#################################")
  	wynik.append(szmaragd)
  	wynik.append(rubin)
  	wynik.append(szafir)
  	wynik.append(beryl)
  	wynik.append(opal)
  	wynik.append(kasa)

  @staticmethod
  def super_motyka_gra(szmaragd, rubin, szafir, beryl, opal, kasa,sakwa_na_mineraly,wynik):
    dzien1kopanie = randint(0,100)
    
    if dzien1kopanie >= 0 and dzien1kopanie <= 20:
      print("\n##############################")
      print("##### WYDOBYTO MINERAŁ! ######")
      print("#### ZDOBYWASZ SZMARAGD #####")
      print("##############################")
      szmaragd = szmaragd + 1
      sakwa_na_mineraly.append("szmaragd")
    elif dzien1kopanie > 20 and dzien1kopanie <= 40:
      print("\n##############################")
      print("##### WYDOBYTO MINERAŁ!  #####")
      print("###### ZDOBYWASZ RUBIN  ######")
      print("##############################")
      rubin = rubin + 1
      sakwa_na_mineraly.append("rubin")
    elif dzien1kopanie > 40 and dzien1kopanie <= 60:
      print("\n##############################")
      print("##### WYDOBYTO MINERAŁ! ######")
      print("####  ZDOBYWASZ SZAFIR ######")
      print("##############################")
      szafir = szafir + 1
      sakwa_na_mineraly.append("szafir")
    elif dzien1kopanie > 60 and dzien1kopanie <= 80:
      print("\n##############################")
      print("##### WYDOBYTO MINERAŁ!  #####")
      print("###### ZDOBYWASZ BERYL  ######")
      print("##############################")
      beryl = beryl + 1
      sakwa_na_mineraly.append("beryl")
    elif dzien1kopanie > 80 and dzien1kopanie <= 100:
      print("\n##############################")
      print("##### WYDOBYTO MINERAŁ! ######")
      print("####  ZDOBYWASZ OPAL #######")
      print("##############################")
      opal = opal + 1
      sakwa_na_mineraly.append("opal")
    wynik.append(szmaragd)
    wynik.append(rubin)
    wynik.append(szafir)
    wynik.append(beryl)
    wynik.append(opal)
class Papier:
  def pkn(p,ptkU,ptkC):
  
    print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")

    odp = input("\nPrzyszedł do ciebie chłopiec z okolicy, chcesz z nim pograć? ")
    if odp == "Tak" or odp == "tak" or odp == "TAK":
      print("\nGracie w papier, kamień, nożyce.")
    #PAPIER-1, KAMIEŃ-2, NOŻYCE-3
      while p < 3:
        wyC = randint(1,3)
        wyb = input("\nCo wybierasz? ")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        if wyb == "papier" and wyC == 1:
          print("-REMIS-")
          p += 1
          print(f"{ptkU} : {ptkC}")
        if wyb == "papier"  and wyC == 2:
          ptkU += 1
          print("-PUNKT DLA CIEBIE-")
          p += 1
          print(f"{ptkU} : {ptkC}")
        if wyb == "papier" and wyC == 3:
          ptkC += 1
          print("-PUNKT DLA CHŁOPCZYKA-")
          p += 1
          print(f"{ptkU} : {ptkC}")
        
              
        if wyb == "kamień" or wyb == "kamien" and wyC == 1:
          print("-PUNKT DLA CHŁOPCZYKA-")
          ptkC += 1
          print(f"{ptkU} : {ptkC}")
          p += 1
        if wyb == "kamień" or wyb == "kamien" and wyC == 2:
          print("-REMIS-")
          print(f"{ptkU} : {ptkC}")
          p += 1
        if wyb == "kamień" or wyb == "kamien" and wyC == 3:
          print("-PUNKT DLA CIEBIE-")
          ptkU += 1
          print(f"{ptkU} : {ptkC}")
          p += 1
        
        if wyb == "nożyce" or wyb == "nozyce" and wyC == 1:
          print("-PUNKT DLA CIEBIE-")
          ptkU += 1
          p += 1
          print(f"{ptkU} : {ptkC}")
        if wyb == "nożyce" or wyb == "nozyce" and wyC == 2:
          print("-PUNKT DLA CHŁOPCZYKA-")
          ptkC += 1
          p += 1
          print(f"{ptkU} : {ptkC}")
        if wyb == "nożyce" or wyb == "nozyce" and wyC == 3:
          print("-REMIS-")
          p += 1
          print(f"{ptkU} : {ptkC}")
    print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-") 
class Licz:
  def __init__(self,p,ptkU,ptkC):
    self.p = p
    self.ptkU = ptkU
    self.ptkC = ptkC

class Kamien(Licz):
  @staticmethod
  def pkn(self):
    print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")

    odp = input("\nPrzyszedł do ciebie chłopiec z okolicy, chcesz z nim pograć? ")
    if odp == "Tak" or odp == "tak" or odp == "TAK":
      print("\nGracie w papier, kamień, nożyce.")
    #PAPIER-1, KAMIEŃ-2, NOŻYCE-3
      while self.p < 3:
        wyC = randint(1,3)
        wyb = input("\nCo wybierasz? ")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        if wyb == "papier" and wyC == 1:
          print("-REMIS-")
          self.p += 1
          print(f"{self.ptkU} : {self.ptkC}")
        if wyb == "papier"  and wyC == 2:
          self.ptkU += 1
          print("-PUNKT DLA CIEBIE-")
          self.p += 1
          print(f"{self.ptkU} : {self.ptkC}")
        if wyb == "papier" and wyC == 3:
          self.ptkC += 1
          print("-PUNKT DLA CHŁOPCZYKA-")
          self.p += 1
          print(f"{self.ptkU} : {self.ptkC}")
        
              
        if wyb == "kamień" or wyb == "kamien" and wyC == 1:
          print("-PUNKT DLA CHŁOPCZYKA-")
          self.ptkC += 1
          print(f"{self.ptkU} : {self.ptkC}")
          self.p += 1
        if wyb == "kamień" or wyb == "kamien" and wyC == 2:
          print("-REMIS-")
          print(f"{self.ptkU} : {self.ptkC}")
          self.p += 1
        if wyb == "kamień" or wyb == "kamien" and wyC == 3:
          print("-PUNKT DLA CIEBIE-")
          self.ptkU += 1
          print(f"{self.ptkU} : {self.ptkC}")
          self.p += 1
        
        if wyb == "nożyce" or wyb == "nozyce" and wyC == 1:
          print("-PUNKT DLA CIEBIE-")
          self.ptkU += 1
          self.p += 1
          print(f"{self.ptkU} : {self.ptkC}")
        if wyb == "nożyce" or wyb == "nozyce" and wyC == 2:
          print("-PUNKT DLA CHŁOPCZYKA-")
          self.ptkC += 1
          self.p += 1
          print(f"{self.ptkU} : {self.ptkC}")
        if wyb == "nożyce" or wyb == "nozyce" and wyC == 3:
          print("-REMIS-")
          self.p += 1
          print(f"{self.ptkU} : {self.ptkC}")
    print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-") 