import time

def intro(): 
    print("Je bent een Poolse inwoner en je land gaat de oorlog met Ukraine joinen om tegen Rusland te vechten en jongens die 18+ zijn moeten de leger in maar dat wil jij  niet.")
    time.sleep(4.0)
    print("dus je wilt vluchten en je gaat vluchten naar Nederland want daar woont je beste vriend Jay waar je kan verblijven en hij woont in Utrecht")
    time.sleep(4.0)
    print("Je hebt 1000 euro opgespaard")
    time.sleep(2.0)
    print("je hebt 4 keuzes om te vluchten de bus, trein , vliegtuig of auto te gaan vluchten naar Nederland.")
    time.sleep(3.0)
    print("kies 1 van de keuzes")

def bus364():
    print("je neemt de eerst volgende bus en als je aan komt dan moet je gewoon voor 10 minuten vanuit de voorkant van de station en je komt aan in zijn straat")
    time.sleep(2.0)
    print("je bent gevlucht en veilig aangekomen bij jay zijn huis...... einde")

def bus408():
    print("je hebt de verkeerde bus gepakt dus je moet vanaf centraal een bus naar utrecht zuid nemen en dan loop je als je aangekomen ongeveer 10 minuten en je komt voor jay zijn huis uit")
    time.sleep(5.0)
    print("je bent gevlucht en veilig aangekomen bij jay zijn huis...... einde")



def hotel():
    print("je gaat dus nu in een hotel slapen in de middel van frankfurt dus het gaat je 250 euro kosten")
    time.sleep(4.0)
    print("de volgende dag koop je weer een dag kaart die je 100 euro kost en jepakt de trein om 12.00 en je komt aan in amsterdam om 16.00")
    time.sleep(4.0)
    print("nu moet je kiezen of je met bus 364 die naar utrecht zuid gaat of bus 408 die naar utrecht centraal")

    for i in range(10):
        choice = input()
        if choice == 'bus 364':
            bus364()
        elif choice == 'bus 408':
            bus408()
        else:
            print("kiez uit bus 364 of bus 408")



def amsterdam():
    print("je hebt besloten om door te rijden dus je pakt de trein om 21:00 en je viel onderweg in slaap en iemand heeft je tas gestolen en de conducteur maakt je wakker om te kijken of je je ticket heb")
    time.sleep(6.0)
    print("jij komt er dan achter dat je tas is gestolen met all je spullen en je ticket")
    time.sleep(2.0)
    print("je praat engels tegen de conducteur en je vertelt hem dat iemand jou tas heeft gestolen met jou ticket en all je spullen er in")
    time.sleep(4.0)
    print("de conducteur gelooft je niet en belt de politie die jou oppaken en je de gevangenis in ben gestuurt")
    time.sleep(3.0)
    print("je bent gepakt en je bent dus niet gevlucht dus je bent gevaalt!!!!!")
    




def stop():
    print("je gaat stoppen om je auto te tenken maar voordat je verder kan rijden na de tanken houd de politie je aan om te kijken of je gekozen ben om naar de leger te gaan of niet zadat ze niet willen dat iedereen vlucht")
    time.sleep(6.0)
    print("na dat ze je papieren en je pasport hebben gevraagt komen ze er achter dat jij geselecteerd was en aan het vluchten was dus ze houden je aan en nemen ze je terug naar de leger")
    time.sleep(6.0)
    print("je bent gepakt en je bent dus niet gevlucht dus je bent gevaalt!!!!!")


def doorrijden():
    print("je rijd door en na de grens is er een kleine dorpje 8 kilometer van de grens waar een tankstation is dus jij kan gerust tanken en daarna doorrijden")
    time.sleep(5.0)
    print("je heb de heledag gereden en je begint moe te worden dus als je langs een stad die oldenberg heet stop je en je besluit te gaan slapen omdat je vloet dat je te moe ben om door te rijden")
    time.sleep(6.0)
    print("in de stad zijn maar 2 hotels op dit tijd nog open")
    time.sleep(2.0)
    print("de ene is recht in de stad en je kan daar slapen voor 200 euro met ochtendeten en de andere is in de randstad en daar kost het 100 euro voor een nacht en ochtendeten")

    for i in range(10):
        choice = input()
        if choice =='hotel in stad':
            hotelinstad()
        elif choice =='hotel in randstad':
            hotelinrandstad()
        else:
            print("kiez uit hotel in stad of hotel in randstad")


def hotelinstad():
    print("nadat je wakker ben geworden en je ontbijt heb gegeten dan rij je rechts streeks weer door naar utrecht en je kom er om 15.00 aan")
    time.sleep(5.0)
    print("je bent gevlucht en veilig aangekomen bij jay zijn huis...... einde")





def hotelinrandstad():
    print("je gaat overnachten in de hotel in de randstad en de volgende dag word je wakker")
    time.sleep(4.0)
    print("toen je wakker werd merkte dat all je spullen waren gestolen en dan keek je uit de raam waaruit je je autokon zien waar hij hoorde te staan")
    time.sleep(6.0)
    print("nu dat all je spullen en auto is gestolen waar alles in zat kan jij niet verder dus het is game over voor jou")
    time.sleep(5.0)
    print("je hebt mislukt om te vluchten omdat halverwegen de weg naar jay jij niet meer door kon!!!!!!")


       














def trein():
    print ("je pakt je tas in met kleren voor 1 week en je pasport en alles wat je nodig hebt")
    time.sleep(4.0)
    print("je koopt een dagkaart die 100 euro kost en je neemt de trein de volgende dag")
    time.sleep(4.0)
    print("the trein is om 8.00 vanaf Warschau naar Frankfurt dan kom je aan om 20:32")
    time.sleep(4.0)
    print ("ga je nu overnachten in een hotel of rij je door ?")

    for i in range(10):
        choice = input()
        if choice == 'overnachten in een hotel':
            hotel()
            break
        elif choice == 'rij je door':
            amsterdam()
        else:
            print("kiez uit rij je door of overnachten in een hotel")


def bus():
    print("je pakt de bus van warschau naar frankfurt de ticket koste je 200 euro de bus rijd om 12.00 en je zou in frankfurt de volgende dag om 16.00 aankomen maar je hebt wel onderweg tussenstops")
    time.sleep(6.0)
    print("de bus stopt bij de grenz tussen polen en duitsland en opeens houd politie de bus tegen om te kijken of er mensen zijn die de land vluchten omdat ze niet de leger in willen")
    time.sleep(7.0)
    print("ze komen er achter tijdens het checken van elke pasagier dat jij probeerde te vluchten dus je word terug mee genomen naar polen en de leger in")
    time.sleep(5.0)
    print("je bent gepakt dus je vlucht is mislukt!!!!!")  





def vliegtuig():
   print("je koopt een ticket om van warschau naar amsterdamte gaan voor 300 euro voor morgen")
   time.sleep(4.0)
   print("je gaat om 6.00 naar de vliegveld omdat je vliegtuig om 12.00 is en het duurt altijd lang")
   time.sleep(3.0)
   print ("als je binnen ben ga je door de poortjes in de vliegveld om naar je vliegtuig te gaan en na de metaaldedectoors kom je aan bij pasport controle en daar heb jij niet over na gedacht")
   time.sleep(3.0)
   print("je kan niet terug dus je moet doorlopen en als ze je pasport checken komen ze er achter dat jij naar de leger moet waardoorc er bewakers komen die je oppakken en je naar de leger mee nemen")
   time.sleep(7.0)
   print("je bent gepakt dus je vlucht is mislukt!!!!!")




def auto():
    print("je pakt all je spullen in en je begint te rijden met de auto")
    time.sleep(3.0)
    print("Je rijd met de auto en je hebt nog maar voor 20 km aan benzine en in 10 km is er een tankstation maar het is wel de grens tussen polen en Duitsland")
    time.sleep(4.0)
    print("stop je of hoop je om nog een tank station 10 kilometer verder te vinden?")
    
    for i in range(10):
        choice = input()
        if choice == 'stop':
            stop()
            break
        elif choice == 'rij verder':
            doorrijden()
        else:
            print("kiez uit stop of rij verder")


























intro()
for i in range(10):
    choice = input()
    if choice == 'trein':
        trein()
    elif choice == 'bus':
        bus()
    elif choice == 'vliegtuig':
        vliegtuig()
    elif choice == 'auto':
        auto()
    else: 
        print ("kiez uit een van de 4 keuzes")
