import csv, configparser, os, shutil, glob, sys, re
from shutil import copyfile, make_archive
from datetime import datetime  
from datetime import timedelta  

ktora_linijka=0
czy_jest_export=0
now = datetime.now()

print(f'Importer Baselinker->Mercateo \n\n')


for file in glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/../incoming/*.csv"):
    czy_jest_export=1
    
if czy_jest_export == 0:
    print(f'Koncze bo nie ma nic do roboty - nie znaleziono eksportow z baselinker w katalogu incoming.\n')
    sys.exit(0)

config_merc = configparser.ConfigParser()
config_merc.read(os.path.dirname(os.path.realpath(__file__)) +'/../config/importer_merc.ini')

for file in glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/../incoming/*.csv"):
    shutil.move(file,os.path.dirname(os.path.realpath(__file__)) + '/../incoming/produkty_baselinker.csv')

copyfile(os.path.dirname(os.path.realpath(__file__)) +'/../templ/products_2082_hilark_template.txt',os.path.dirname(os.path.realpath(__file__)) +'/../out/products_2082_pol_UTF-8.txt')
copyfile(os.path.dirname(os.path.realpath(__file__)) +'/../templ/availability-data-catalog-2082_template.csv',os.path.dirname(os.path.realpath(__file__)) +'/../out/availability-data-catalog-2082.csv')
with open(os.path.dirname(os.path.realpath(__file__)) +'/../incoming/produkty_baselinker.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    with open(os.path.dirname(os.path.realpath(__file__)) +'/../out/products_2082_pol_UTF-8.txt', 'a') as csvfile:
        wynikowyCSV = csv.writer(csvfile, delimiter=';', escapechar='\\', quoting=csv.QUOTE_NONE ) # quotechar='', quoting=csv.QUOTE_MINIMAL
        for row in csv_reader:
            if ktora_linijka == 0:
                ktora_linijka+=1
            else:
                dlugi_opis=row[9].replace('"','')
                # dlugi_opis=dlugi_opis.replace('<section class=text-item>','')
                # dlugi_opis=dlugi_opis.replace('<section class=section>','')
                # dlugi_opis=dlugi_opis.replace('</section>','')
                #dlugi_opis=dlugi_opis.replace('<section(.*)>','')
                # dlugi_opis=re.sub(r"<section(.*?)>",r"",dlugi_opis)
                # dlugi_opis=dlugi_opis.replace('<div class=item item-12>','')
                # dlugi_opis=dlugi_opis.replace('size=3','')
                # dlugi_opis=dlugi_opis.replace('font-family','')
                #dlugi_opis=dlugi_opis.replace('font-size','')
                # dlugi_opis=dlugi_opis.replace('<h1>','')
                # dlugi_opis=dlugi_opis.replace('<span','')
                # dlugi_opis=dlugi_opis.replace('<div','')

                # dlugi_opis=dlugi_opis.replace('</font>','')
                # dlugi_opis=dlugi_opis.replace('</span>','')
                # dlugi_opis=dlugi_opis.replace('</div>','')
                # print(f'przed nr: {row[0]} opis: {dlugi_opis}')
                # dlugi_opis=dlugi_opis.replace('face=Arial size=3>','')
                dlugi_opis=re.sub(r"<font(.*?)>",r"",dlugi_opis)
                # print(f'po {dlugi_opis}')
                dlugi_opis=re.sub(r"<section(.*?)>",r"",dlugi_opis)
                dlugi_opis=re.sub(r"<div(.*?)>",r"",dlugi_opis)
                dlugi_opis=re.sub(r"<span(.*?)>",r"",dlugi_opis)
                dlugi_opis=dlugi_opis.replace('			','')
                dlugi_opis=dlugi_opis.replace('\n','')
                dlugi_opis=dlugi_opis.replace('\t','')
                dlugi_opis=dlugi_opis.replace('\r','')
                dlugi_opis=dlugi_opis.replace('&nbsp;',' ')
                dlugi_opis=dlugi_opis.replace(';','')
                dlugi_opis=dlugi_opis.replace('src=','')
                dlugi_opis=dlugi_opis.replace('Wysyłka w 24 h a dostawa max 2 dni robocze.','')
                dlugi_opis=dlugi_opis.replace('Więcej informacji pod telefonem +48 12 376 74 64','')
                dlugi_opis=dlugi_opis.replace('Więcej informacji na www.hilark.eu','')
                dlugi_opis=dlugi_opis.replace('więcej informacji na www.hilark.eu','')
                dlugi_opis=dlugi_opis.replace('MASZ PYTANIA DZWOŃ + 12 3 767 464','')
                dlugi_opis=dlugi_opis.replace('Wysyłka 24h w dni robocze - opcja kurier','')
                dlugi_opis=dlugi_opis.replace('Wiecej informacji +123 767 464','')
                dlugi_opis=dlugi_opis.replace('Więcej informacji','')
                dlugi_opis=dlugi_opis.replace('WYSTAWIAMY FAKTURY VAT','')
                dlugi_opis=dlugi_opis.replace('+12 376 74 64','')
                dlugi_opis=dlugi_opis.replace('www.hilark.eu','')
                dlugi_opis=dlugi_opis.replace('Zadzwoń zapytaj podpowiemy i doradzimy 123 767 464 numer stacjonarny','')
                dlugi_opis=dlugi_opis.replace('masz pytania, zadzwoń telefon 12 376 74 64','')
                dlugi_opis=dlugi_opis.replace('Masz pytania zadzwoń 12 376 74 64','')
                dlugi_opis=dlugi_opis.replace('Masz pytania zadzwoń 123 767 464','')
                dlugi_opis=dlugi_opis.replace('Masz pytania zadzwoń +48 123 767 464','')
                dlugi_opis=dlugi_opis.replace('ZADZWOŃ','')
                dlugi_opis=dlugi_opis.replace('zadzwoń, zapytaj 123767464','')
                dlugi_opis=dlugi_opis.replace('zadzwoń, porozmawiajmy, bądź pewien co kupujesz  tel:','')
                dlugi_opis=dlugi_opis.replace('123 767 464','')
                dlugi_opis=dlugi_opis.replace('Polecamy kontakt telefoniczny  +12 3 767 464','')
                dlugi_opis=dlugi_opis.replace('BĄDŹ PEWNY co kupujesz, zostaw telefon oddzwonimy','')
                dlugi_opis=dlugi_opis.replace('pod telefonem +48','')
                dlugi_opis=dlugi_opis.replace('1 komplet = 100 szt','1 komplet tulejek to 100 tulejek i jest to 1 szt produktu kupowanego')
                separator="Wystawiamy faktury"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="(7-00 do 19-00)"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="Pn - Pt"                
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="pod telefonem"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="kontakt telefoniczny"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="Wysyłka"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="Pracujemy"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="pracujemy"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="W przypadku pytań"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="MASZ PYTANIA"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="ZAPYTAJ"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                separator="+48 12 376 74 64"
                dlugi_opis=dlugi_opis.split(separator,1)[0]
                
                kategoria_liczbowa=row[5].replace('Dom i Ogród/Budownictwo i Akcesoria/Elektryka i akcesoria/','')
                kategoria_liczbowa=kategoria_liczbowa.replace('Gniazda','201')
                kategoria_liczbowa=kategoria_liczbowa.replace('Kable i przewody','202')
                kategoria_liczbowa=kategoria_liczbowa.replace('Przedłużacze','203')
                kategoria_liczbowa=kategoria_liczbowa.replace('Pozostałe','204')

                if (("wzmocniony" in row[1]) or ("H05VVF" in row[1])):
                    karata_produktu="karta_H05VV-F_H05VVH2-F_HILARK.pdf"
                else:
                    karata_produktu="karta_danych_1.pdf"

                wynikowyCSV.writerow([row[0],row[4],row[1],dlugi_opis,row[0],'Hilark','net_list',round(float(row[6])*config_merc.getfloat('FINANSOWE','mnoznik_ceny'),2),'','',1,now.strftime("%d.%m.%Y"),(datetime.now() + timedelta(days=config_merc.getint('FINANSOWE','waznosc_ceny'))).strftime("%d.%m.%Y"),'PLN',config_merc.getfloat('FINANSOWE','stawka_VAT'),config_merc.getint('DOSTAWA','czas_dostawy'),'C62','','',config_merc.getint('ZAMOWIENIE','min_zam'),1,row[5].replace('Dom i Ogród/Budownictwo i Akcesoria/Elektryka i akcesoria/',''),kategoria_liczbowa,'normal','',row[12].rsplit('/', 1)[1], \
                    'normal','','','','','','','','','','','','','','','','',karata_produktu,'data_sheet','Karta danych produktu','','','','','','','','','','napięcie','500','V','prąd','3','A'])
                ktora_linijka+=1
print(f'Zaimportowalem {ktora_linijka} produktow z Baselinker.')

ktora_linijka=0
sciezka_img = os.path.dirname(os.path.realpath(__file__)) + "/../img/"

#  Zaciąganie zdjec z Baselinkera: --------------------------------------------------------
ktora_linijka=0
with open(os.path.dirname(os.path.realpath(__file__)) +'/../incoming/produkty_baselinker.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        if ktora_linijka == 0:
            ktora_linijka+=1
        else:
            
            # DO USUNIECIA: r = requests.get(row[12])
            # DO USUNIECIA: open(row[12].rsplit('/', 1)[1] , 'wb').write('img/' + r.content)
            
            # Ponizsze odhaszowac aby zaladowac swieze zdjecia (czasochlonne)

            #print(f'Sciagam {row[12]}...\r')
            #os.system(f"""wget -c -N -O "{sciezka_img}{row[12].rsplit('/', 1)[1]}" --read-timeout=5 --tries=0 {row[12]}""")
            #ktora_linijka+=1
# ------------------------------------------------------------------------------------------

# Zaciaganie stanow magazynowych z baselinkera ---------------------------------------------
ktora_linijka=0
with open(os.path.dirname(os.path.realpath(__file__)) +'/../incoming/produkty_baselinker.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    with open(os.path.dirname(os.path.realpath(__file__)) +'/../out/availability-data-catalog-2082.csv', 'a') as csvfile:
        wynikowyCSV = csv.writer(csvfile, delimiter=';', escapechar='\\', quoting=csv.QUOTE_NONE ) # quotechar='', quoting=csv.QUOTE_MINIMAL
        for row in csv_reader:
            if ktora_linijka == 0:
                ktora_linijka+=1
            else:
                wynikowyCSV.writerow([row[0],row[2]])
                ktora_linijka+=1
# ------------------------------------------------------------------------------------------             
print(f'Sciagnalem {ktora_linijka} zdjec produktowych z Baselinker.\nRozpoczynam pakowanie zdjec ZIPem...\r')
make_archive('images','zip',root_dir=sciezka_img,base_dir=None)
shutil.move("images.zip", os.path.dirname(os.path.realpath(__file__)) + "/../out/images.zip")

print(f'Rozpoczynam pakowanie kart produktu ZIPem...')
make_archive('pdf','zip',root_dir=os.path.dirname(os.path.realpath(__file__)) + "/../pdf/",base_dir=None)
shutil.move("pdf.zip", os.path.dirname(os.path.realpath(__file__)) + "/../out/pdf.zip")

shutil.move(os.path.dirname(os.path.realpath(__file__)) +'/../incoming/produkty_baselinker.csv',os.path.dirname(os.path.realpath(__file__)) +'/../old/produkty_baselinker.csv')

print(f'Importer Baselinker->Mercateo - Wersja: 20v0316\n\n')
print(f'\nKoniec dzialania importera.')