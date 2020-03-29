import configparser, os, shutil, glob, sys, re, time,fileinput
from shutil import copyfile, make_archive
from datetime import datetime  
from datetime import timedelta  

ktora_linijka=0
czy_jest_export=0
now = datetime.now()

print(f'Importer Baselinker->Morele\n\n')

#===========Przygotowanie pliku importu=====================================================================
for file in glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/../incoming/*.xml"):
    czy_jest_export=1
    
if czy_jest_export == 0:
    print(f'Koncze bo nie ma nic do roboty - nie znaleziono eksportow Ceneo XML z baselinker w katalogu incoming.\n')
    sys.exit(0)

config_merc = configparser.ConfigParser()
config_merc.read(os.path.dirname(os.path.realpath(__file__)) +'/../config/importer_merc.ini')

for file in glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/../incoming/*.xml"):
    shutil.move(file,os.path.dirname(os.path.realpath(__file__)) + '/../incoming/produkty_zbaselinker.xml')
shutil.copy(os.path.dirname(os.path.realpath(__file__)) +'/../incoming/produkty_zbaselinker.xml',os.path.dirname(os.path.realpath(__file__)) +'/../old/produkty_zbaselinker_copy.xml')
#============================================================================================================
plik = os.path.dirname(os.path.realpath(__file__)) +'/../incoming/produkty_zbaselinker.xml'

for linia in fileinput.input(plik, inplace=True):
    print(linia.replace("&lt;","<"), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace("&gt",">"), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace('stock','avail="1" stock'), end='')
for linia in fileinput.input(plik, inplace=True):
    print(re.sub('<font(.*?)>','',linia),end='')
for linia in fileinput.input(plik, inplace=True):
    print(re.sub('<section(.*?)>','',linia),end='')
for linia in fileinput.input(plik, inplace=True):
    print(re.sub(r"<div(.*?)>",r"",linia), end='')
for linia in fileinput.input(plik, inplace=True):
    print(re.sub(r"<span(.*?)>",r"",linia), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace("	;",""), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace(";",""), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace("nbsp",""), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace("</font>",""), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace("</section>",""), end='')
for linia in fileinput.input(plik, inplace=True):
    print(linia.replace("</div>",""), end='')
    # linia.replace('			','')
    # linia.replace('&nbsp;',' ')
    # linia.replace(';nbsp;',' ')
    # linia.replace(';','')
    # linia.replace('Wysyłka w 24 h a dostawa max 2 dni robocze.','')
    # linia.replace('Więcej informacji pod telefonem +48 12 376 74 64','')
    # linia.replace('Więcej informacji na www.hilark.eu','')
    # linia.replace('więcej informacji na www.hilark.eu','')
    # linia.replace('MASZ PYTANIA DZWOŃ + 12 3 767 464','')
    # linia.replace('Wysyłka 24h w dni robocze - opcja kurier','')
    # linia.replace('Wiecej informacji +123 767 464','')
    # linia.replace('Więcej informacji','')
    # linia.replace('WYSTAWIAMY FAKTURY VAT','')
    # linia.replace('+12 376 74 64','')
    # linia.replace('www.hilark.eu','')
    # linia.replace('Zadzwoń zapytaj podpowiemy i doradzimy 123 767 464 numer stacjonarny','')
    # linia.replace('masz pytania, zadzwoń telefon 12 376 74 64','')
    # linia.replace('Masz pytania zadzwoń 12 376 74 64','')
    # linia.replace('Masz pytania zadzwoń 123 767 464','')
    # linia.replace('Masz pytania zadzwoń +48 123 767 464','')
    # linia.replace('ZADZWOŃ','')
    # linia.replace('zadzwoń, zapytaj 123767464','')
    # linia.replace('zadzwoń, porozmawiajmy, bądź pewien co kupujesz  tel:','')
    # linia.replace('123 767 464','')
    # linia.replace('Polecamy kontakt telefoniczny  +12 3 767 464','')
    # linia.replace('BĄDŹ PEWNY co kupujesz, zostaw telefon oddzwonimy','')
    # linia.replace('pod telefonem +48','')
    # linia.replace('1 komplet = 100 szt','1 komplet tulejek to 100 tulejek i jest to 1 szt produktu kupowanego')
    # separator="Wystawiamy faktury"
    # linia.split(separator,1)[0]
    # separator="(7-00 do 19-00)"
    # linia.split(separator,1)[0]
    # separator="Pn - Pt"                
    # linia.split(separator,1)[0]
    # separator="pod telefonem"
    # linia.split(separator,1)[0]
    # separator="kontakt telefoniczny"
    # linia.split(separator,1)[0]
    # separator="Wysyłka"
    # linia.split(separator,1)[0]
    # separator="Pracujemy"
    # linia.split(separator,1)[0]
    # separator="pracujemy"
    # linia.split(separator,1)[0]
    # separator="W przypadku pytań"
    # linia.split(separator,1)[0]
    # separator="MASZ PYTANIA"
    # linia.split(separator,1)[0]
    # separator="ZAPYTAJ"
    # linia.split(separator,1)[0]
    # separator="+48 12 376 74 64"
    # linia.split(separator,1)[0]


    # wynikowy= open(os.path.dirname(os.path.realpath(__file__)) +'/../out/produkty_zbaselinker.xml','w')
    # wynikowy.write(zrodlowy)
    # wynikowy.close()

#================Dodanie daty do nazwy XML=======================================================================
# os.remove(os.path.dirname(os.path.realpath(__file__)) +'/../incoming/produkty_zbaselinker.xml')

for file in glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/../incoming/produkty_zbaselinker.xml"):
    shutil.move(file,os.path.dirname(os.path.realpath(__file__)) + '/../out/produkty_baselinker_' + time.strftime("%Y%m%d") + '.xml')
#=================================================================================================================

print(f'Zaimportowalem {ktora_linijka} produktow z Baselinker.')

ktora_linijka=0


print(f'Importer Baselinker->Morele - Wersja: 20v0206\n\n')
print(f'\nKoniec dzialania importera.')