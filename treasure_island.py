import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bine te-am gasit aventurierule!\nAceasta este provocarea insulei amazoanelor!\nCrezi ca poti fura Diamantul Printesei Eveline pentru a il vinde si sa te imbogatesti?\nIncearca daca ai tupeu!\nSucces!")
print("*******************************************************************************")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
aventura = input("Te aventuriezi pe insula amazoanelor incercand sa furi Diamantul Printesei Eveline?\n > da sau nu:  ")
if aventura == "da":
  print("Ajungi intr-un port cu mai multe barci si vapoare.\nO data ajuns in port trebuie sa alegi in care barca vei urca,")
  time.sleep(2)
  print("Citind manifestul public al transporturilor afli ca sunt 3 barci ce se vor deplasa astazi si toate vor naviga pe langa insula amazoanelor:")
  time.sleep(1)
  print(" - Prima barca este un vapor de transport persoane cu un aspect modern ancorat la debarcaderul numarul 1.")
  time.sleep(1)
  print(" - A doua barca este o barca de pescari usor ruginita in partea stanga ancorata la debarcaderul numarul 2.")
  time.sleep(1)
  print(" - Iar ce-a de-a treia barca este un vapor ce transporta carbune peste ocean si se afla la debarcaderul numarul 3.")
  time.sleep(2)
  choice1 = input(" > Spre care debarcader te indrepti? 1, 2 sau 3?:  ")
  if choice1 == "1":
    print("Te indrepti spre vaporul de croaziera insa stii ca nu ai bilet asa ca te strecori printre ospatari si te dai drept ospatar pentru a urca pe vapor.")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(5)
    print("...")
    time.sleep(1)
    print("La fel ca si restul 'colegilor' tai, esti intampinat de un barbat ce statea la imbarcarea staff-ului.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(3)
    print("...")
    time.sleep(1)
    nume1 = input("Intampinandu-te cu o privire rece si nepasatoare barbatul te intreaba:\n - Iar tu cum te numesti?\n")
    print(f"Cu aceeasi nepasare ca si adineauri, Barbatul iti spune:\n - Bun venit {nume1}, te poti imbarca pe vapor.\n - NEEEEEXT!")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(5)
    print("...")
    time.sleep(1)
    print("Ai urcat pe vaporul de croaziera iar in cateva minute deja te afli in largul marii.")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(5)
    print("...")
    time.sleep(1)
    print("Aflandu-te pe puntea vaporului de croaziera printre oameni observi in fata ta o femeie frumoasa ce iesea in evidenta din restul multimii.")
    time.sleep(2)
    print("Era o femeie inalta, bruneta cu parul lung peste umeri imbracata cu o camasa alba, o fusta neagra ce se lungea aproape de genunchi,\nsi niste tocuri negre ce o facea sa para giganta in comparatie cu alte femei.")
    time.sleep(6)
    print("..")
    time.sleep(12)
    print("...")
    time.sleep(1)
    print("Timp de cateva secunde bune ai pierdut notiunea timpului admirand femeia bruneta.")
    time.sleep(2)
    print("Insa privirile tale nu au trecut neobservate si fara sa iti dai seama aceeasi femeie inalta acum se indrepta spre tine cu privirea atintita asupra ta.")
    time.sleep(6)
    print("...")
    time.sleep(1)
    print("Ajunsa in fata ta, cu o expresie iritata, femeia iti vorbeste:")
    time.sleep(2)
    print(f"- Presupun ca tu esti {nume1}, te-am cautat tot vaporul, de ce nu esti costumat?")
    time.sleep(2)
    print("Fiind presat de situatie, te poti gandi doar la 2 raspunsuri:\n - As putea sa-i spun sa se duca dracului\n - Sau as putea sa par confuz")
    time.sleep(2)
    answer1 = input("Oare ce sa ii raspund?\n > Varianta 1 sau 2?  ")
    if answer1 == "1":
      print("Fara nici-o ezitare si cu durere in pula ii spun:")
      time.sleep(2)
      print("- Ce pula mea vrei tu?")
      time.sleep(5)
      print("Extrem de confuza si cu ochii bulbucati femeia iti raspunde:")
      time.sleep(5)
      print("- Poftim??")
      time.sleep(2)
      print("Socata de raspunsul tau, femeia scoate o statie ce o avea prinsa de fusta in partea dreapta, o duce la gura si apasa un buton:")
      time.sleep(5)
      print("- Paza! Am nevoie de cineva urgent pe puntea din fata!")
      time.sleep(5)
      print("Fara sa ai timp de reactie 2 barbati ce semanau mai mult cu niste gorile decat oameni te prind din lateral,\nunul de mana stanga si celalalt de mana dreapta.")
      time.sleep(5)
      print(f"Femeia le spune celor 2:\n-Va rog sa escortati pe {nume1} catre puntea 2B si oferitii o celula din cele 5 existente.")
      time.sleep(5)
      print(f"- Nu-mi amintesc sa fi angajat impertinenti in staff-ul meu si trebuie sa ii fac o verificare lui {nume1}.")
      time.sleep(5)
      print("Fara sa mai ai vreo solutie, cele 2 gorile te apuca fortat de maini si te duc spre o punte inferioara a vaporului unde te inchid intr-o celula.")
      time.sleep(3)
      print("...")
      time.sleep(10)
      print("Singur intr-o celula, dintr-o incapere intunecata si fara scapare,\n pare ca nu mai ai nici-o sansa sa iti atingi obiectivul si cine stie ce fel de soarta cruda te asteapta aici.")
      time.sleep(10)
      print("GAME OVER - Ai fost incarcerat fara scapare.")
    elif answer1 == "2":
      print("Pentru a nu ma da de gol ii raspund:\n- Buna ziua doamna!")
      time.sleep(1)
      print("- Sunt putin confuz, este prima data cand lucrez pe un vapor de croaziera si nu stiu ce sa fac")
      time.sleep(5)
      print("- Si .. imi e putin cam greu sa recunosc dar am niste emotii de nu stiu ce-i cu mine.")
      time.sleep(5)
      print("Dintr-o data un zambet rasare pe din coltul buzelor rosii rujate ale femeii si iti raspunde:")
      time.sleep(5)
      print("- Ahahaha, cu un ras isteric femeia continua:\n- Probabil esti nou puiule.")
      time.sleep(2)
      print("- Uite, in primul rand ar trebui sa mergi in camera ospatarilor si sa te costumezi corespunzator")
      time.sleep(5)
      print("- Nu poti servi in carpele acestea cu care esti imbracat, fara suparare dar avem niste standarde de mentinut.")
      time.sleep(7)
      print("- Dupa ce te-ai imbracat corespunzator, cauta-ma si o sa iti spun ce trebuie sa faci mai departe.")
      time.sleep(5)
      print(f"- Ce mai astepti {nume1}??\n- Da-i drumul si costumeaza-te!")
      time.sleep(5)
      print("Cu capul in pamant, pentru a nu ma da de gol, inghit in ciuda si pornesc spre cabina ospatarilor.")
      time.sleep(2)
      print(".")
      time.sleep(2)
      print("..")
      time.sleep(4)
      print("...")
      print("Ajung in fata unei usi pe care scria mare: CABINA SERVITORILOR")
      time.sleep(4)
      print("Pentru ca vreau sa ajung pe insula amazoanelor intru in cabina, cu capul in pamant pentru a nu atrage si mai multe priviri.")
      time.sleep(4)
      print("Ma costumez intr-o tinuta eleganta de ospatar si ma indrept inapoi spre puntea principala")
      time.sleep(2)
      print("..")
      time.sleep(4)
      print("...")
      time.sleep(1)
      print("Acea femeie ramasese exact in acelasi loc iar acum statea de vorba cu 2 barbai.")
      time.sleep(2)
      print("Apropriindu-te realizezi ca acei 2 barbati, care semanau mai mult cu 2 gorile decat cu oamenii, erau de fapt niste pazinici.")
      time.sleep(5)
      print("Dintr-o data te cuprinde paranoia si transpiri pe loc, gandindu-te oare ce s-ar fi intamplat daca i-as fi raspuns diferit femeii...")
      time.sleep(5)
      print("Ajuns acum din nou langa femeia bruneta, cei 2 barbati se retrag si isi vad de treaba,")
      time.sleep(5)
      print("Pentru ca acum am avut timp de gandire m-am gandit la mai multe solutii si as putea:\n")
      time.sleep(2)
      print(" - Sa incerc sa o seduc si poate sa am parte de niste aventura pe drum\n - Sa imi continui rolul de ospatar\n - Sau as putea sa incerc sa ma imprietenesc cu ea")
      answer2 = input("Ce varianta de abordare sa aleg?\n > Varianta 1, 2 sau 3?  ")
      if answer2 == "1":
        print("Fara sa ma gandesc prea mult si cu o dorinta de a ma razbuna pe ea dominando ii spun femeii inalte:")
        time.sleep(2)
        print("- Papusa, uite, suntem intr-o croaziera, asa ca haide sa ne simtim bine impreuna si sa-l facem fericit pe Dumnezeu!")
        time.sleep(5)
        print("Socata fiind femeia de afirmatia ta, incearca sa iti raspunda inapoi insa...")
        time.sleep(5)
        print("Din stanga ei, la doar 1 metru departare iese un barbat din multime si cu o expresie nervoasa spune:")
        time.sleep(7)
        print("- Baga-mi-as pula in coastele tale!")
        time.sleep(2)
        print("- Te dai la nevasta-mea?!")
        time.sleep(4)
        print("Panicat de ce se intampla nu realizezi ca barbatul acela tocmai scosese un briceag de buzunar si acum il avea in mana.")
        time.sleep(6)
        print("Insa a fost prea tarziu si pana sa realizezi ce se petrece, acel barbat a infpit briceagul in pieptul tau.")
        time.sleep(4)
        print("....")
        time.sleep(6)
        print("Cazi pe spate, cu un briceag infipt in plexul solar, desi este o vreme insorita pentru tine totul se intuneca...")
        time.sleep(4)
        print("......")
        time.sleep(4)
        print("GAME OVER - Ai murit cu un cutit infip in piept.")
      elif answer2 == "2":
        print("Aleg sa nu imi complic viata mai mult decat e si ii spun doamnei brunete:")
        time.sleep(3)
        print(" - Doamna, ati spus sa revin dupa ce m-am echipat si uitati-ma aici.")
        time.sleep(5)
        print("Cu o privire dezgustata femeia iti raspunde:")
        time.sleep(3)
        print("- Ah, aici erai, foarte bine.")
        print("- Mergi si intreaba oamenii daca vor sa fie serviti cu ceva, chiar nu ai mai lucrat deloc ca si ospatar?")
        time.sleep(5)
        print("Nu apuci sa ii zici nimic cand din multime la 1 metru departare se apropie un barbat, crunt la fata.")
        time.sleep(5)
        print("Acel barbat te priveste cu o privire suspicioasa in timp ce strange din pumni si spune:")
        print("- Draga mea. Aici erai. Cine e acesta?")
        time.sleep(7)
        print("Femeia ii raspunde:")
        print(f"- Unul dintre ospatarii vasului, se numeste {nume1} si nu a mai lucrat pana acum ca si ospatar asa ca tocmai ii dadeam instructiuni.")
        time.sleep(10)
        print("Barbatul iti arunca o privire dezgustata si ii spune femeii:")
        print("- Hmmm, da. Hai sa mergem in cabina sa vorbim ceva.")
        time.sleep(10)
        print("La scurt timp cei 2 se indeparteaza de tine si esti lasat sa iti faci treaba de ospatar")
        time.sleep(5)
        print("Avand acum libertate deplina te indrepti spre spatele vaporului unde ar fi mai putni populat,\ngandindu-te ca aici nu o sa atragi atat de multa atentie.")
        time.sleep(3)
        print("........")
        time.sleep(3)
        print("Alegi sa te pitesti pe langa o cabina unde nu era nimeni, pe usa scriind doar: BUCATARIE")
        time.sleep(6)
        print("Nu realizezi dar adormi langa acea cabina...")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("!!!")
        time.sleep(1)
        print("Esti trezit de o bubuitura uriasa!\nIar cand deschizi ochii realizezi ca usa de la bucatarie fusese explodata si aruncata din balamale!\nIn jurul tau acum era doar foc dar...")
        time.sleep(5)
        print("Nu doar in jur caci mirosul de carne arsa si o durere agonizanta te-a facut sa realizezi ca ai luat foc!")
        time.sleep(5)
        print("!!!")
        time.sleep(5)
        print("GAME OVER - Ai ars de viu.")
      elif answer2 == "3":
        print("Incercand sa ies din situatia in care sunt si sa imi imbunatatesc sederea pe vapor ii spun femeii inalte:")
        time.sleep(5)
        print(f"- Buna din nou! Cred ca am inceput cu stangul, asa ca da-mi voie sa ma prezint cum trebuie, eu sunt {nume1} si sunt incantat sa te intalnesc.")
        time.sleep(5)
        print("- Tu cum te numesti?")
        time.sleep(5)
        print("Cu un zambet dragut, femeia iti intinde mana sa te salute si iti raspunde:")
        time.sleep(5)
        print("- Eu sunt....")
        time.sleep(3)
        print("Inainte sa termine femeia de rostit numele ei, din multime la doar 1 metru departare iese un barbat furios,")
        time.sleep(5)
        print("Pentru ca l-ai observat la timp te-ai dat in spate insa femeia nu a avut timp de reactie,")
        time.sleep(5)
        print("Stupefiat realizezi ca acel barbat tocmai scosese un briceag din buzunar si inainte sa spui ceva deja o injunghiase pe biata femeie pe la spate")
        time.sleep(7)
        print("Cu o furie criminala barbatul urla:\n - Futu-ti mortii ma-tii de femeie!\n - Stiam ca ma inseli!")
        time.sleep(7)
        print("Femeia bruneta zacea pe jos intr-o balta de sange si cu un cutit infipt in spate\nAcum privirea barbatului era pe tine!")
        time.sleep(7)
        print("Realizand ca s-ar putea sa ai aceeasi soarta, fugi cat te tin picioarele catre balustrada vaporului si sari in apa.")
        time.sleep(8)
        print("Tinandu-te la suprafata apei, barbatul nu te urmeaza,\ninsa realizezi prea tarziu ca ai luat o decizie emotiva cand te-ai speriat si ai sarit in apa.")
        time.sleep(8)
        print("Aflandu-te acum in apa iar vaporul inaintand in fata, esti tras sub apa neputincios de elicele motoarelor ce se invarteau cu putere.")
        time.sleep(8)
        print("Prea tarziu realizezi ce decizie fatala ai ales acum fiind sub apa, dintr-o data nu iti mai simti picioarele")
        time.sleep(2)
        print("!!")
        time.sleep(5)
        print("!!!!!!")
        time.sleep(1)
        print("GAME OVER - Ai fost transat de elicele motoarelor.")
  elif choice1 == "2":
    print("Gandindu-te ca ai avea sanse bune sa te strecori printre pescari, te indrepti spre debarcaderul numarul 2.")
    time.sleep(2)
    print("...")
    time.sleep(5)
    print("Fiind destul de sigur pe tine, fiindca in tinerete obisnuiai sa mergi la peste cu tatal tau,\nurci pe barca perscarilor si nimeni de acolo nu pare sa se indoiasca de tine.")
    time.sleep(2)
    print("..")
    time.sleep(4)
    print("....")
    time.sleep(2)
    print("Acum te afli pe mare, intr-o barca de pescari probabil apartinand unei companii te gandesti dupa ce vezi sigla de pe cabina capitanului.")
    time.sleep(2)
    print("In timp ce te aflai langa balustrada vasului privind catre apus, 2 dintre pescari vin la tine si incep sa strige:")
    time.sleep(2)
    print("- Oi, you!")
    time.sleep(2)
    print("Nestiind daca sa raspunzi sau nu te gandesti la ce optiuni ai:")
    print(" - As putea sa ii ignor\n - As putea sa le raspund si sa fiu prietenos cu ei\n - Sau as putea sa fiu agresiv cu ei")
    choice2 = input("Ce fel de abordare dintre cele 3 sa aleg? 1, 2 sau 3?  ")
    if choice2 == "1":
      print("Te gandesti oare de ce te-ar interesa de 2 pescar si ca ar fi mai bine sa ii ignori, poate se simt prost si pleaca.")
      time.sleep(5)
      print("Continui sa te uiti inspre apus cand auzi un al doilea strigat din spate: ")
      print("- Oi, mate! You deaf or stupid?")
      time.sleep(7)
      print("Continui sa ii ignori pe cei 2 pescari cand dintr o data...")
      time.sleep(5)
      print("Simti 2 maini pe piciorul drept si 2 maini pe piciorul stang si inainte sa raspunzi esti aruncat peste bord!")
      time.sleep(7)
      print("Nu poti vedea din apa in barca dar auzi pe unul dintre pescari vorbind:")
      time.sleep(2)
      print("- Have fun sleeping with the fish, maybe they are better company!")
      print("Poti sa ii auzi pe cei 2 pescari cum rad in hohote")
      time.sleep(7)
      print("Incerci sa strigi cat te tin plamanii insa pare ca nimeni nu te aude iar vaporul cu pescari nu face decat sa se indeparteze de tine.")
      time.sleep(10)
      print("Esti singur pe mare... Vaporul cu pescari a disparut in zare iar tu intri in disperare....")
      time.sleep(7)
      print("Afara incepe sa se intunece insa poti vedea in zare o insula, oare poti sa inoti pana acolo te intrebi?")
      time.sleep(7)
      print("Incerci sa innoti inspre insula si poti auzi in jurul tau cum apa se misca... de parca nu ai fi singur.")
      time.sleep(5)
      print("Fara sa realizezi ce se intampla simti dintr-o data o durere devastatoare la piciorul drept si esti tras sub apa de un rechin!")
      time.sleep(5)
      print("Din stanga mai vine un rechi care iti smulge mana stanga!")
      time.sleep(5)
      print("Urmat de alt rechin care te apuca de cap si tot ce poti vedea acum este negru....")
      time.sleep(5)
      print("Pana si durerea incepe sa dispara...")
      time.sleep(5)
      print("GAME OVER - Ai sfarsit mancat de rechini.")
    elif choice2 == "2":
      print("Fiindca nu vreau necazuri decid sa fiu prietenos si le raspund inapoi:")
      time.sleep(5)
      print("- Salut prieteni!\n- Cu ce va pot ajuta?")
      time.sleep(5)
      print("Cei 2 pescari se uita unul la celalalt confuz si inainte sa realizezi ce se intampla...")
      time.sleep(5)
      print("Unul dintre ei iti da un pumn in nas, incepi sa sangerei si te ia cu ameteala, acum nu mai poti judeca...")
      time.sleep(5)
      print("Cazi la pamant si il vezi pe al doilea pescar cum apuca o franghie...")
      time.sleep(5)
      print("Fiind ametit, unul dintre pescari te intoarce cu fata in jos iar celalalt infasoara franghia in jurul gatului tau...")
      time.sleep(2)
      print("!!!!")
      time.sleep(2)
      print("!!!!!!!!!!!")
      time.sleep(2)
      print("Simti ca nu poti respira!")
      time.sleep(2)
      print("Ti se infunda auzul...")
      time.sleep(2)
      print("Auzi din spatele tau:\n- Yea thought ya be smart and you wont get caught ey?")
      time.sleep(5)
      print("Totul se intuneca... nu mai ai putere sa te zbati...")
      time.sleep(5)
      print("GAME OVER - Ai murit sufocat.")
    elif choice2 == "3":
      print("Fiind intr-un mediu necunoscut decizi sa fii agresiv cu ei si sa nu te lasi calcat in picioare!")
      time.sleep(5)
      print("Te uiti la ei urat si te pui intr-o postura gata de atac!")
      time.sleep(5)
      print("Cei 2 nu ezita nici ei si intra in garda!")
      time.sleep(5)
      print("Inainte ca oricare dintre voi sa actioneze auzi o voce:")
      time.sleep(5)
      print("- Oi! You three slackers! Drag your bloody asses back ta work!")
      time.sleep(5)
      print("Cei 2 pescari par acum ingrijorati si te lasa in pace, fiecare luand o undita in mana si mergand in alta parte a vasului.")
      time.sleep(5)
      print("Ca sa nu fii suspect, iei si tu o undita si te duci intr-un loc retras al vasului unde incepi sa pescuiesti.")
      time.sleep(5)
      print("Timpul trece si se insereaza...")
      time.sleep(5)
      print("In timp ce pescuiai in zare poti vedea o insula!")
      time.sleep(5)
      print("Iti spui in minte:\n-Asta trebuie sa fie insula amazoanelor!")
      time.sleep(5)
      print("In timp ce te uitai spre insula te gandesti daca ar trebui sa faci ceva..")
      print("Probabil ca ai putea sa sari din barca si sa innoti pana la mal ori sa astepti pana ce nava va ancora pe insula.")
      choice3 = input("Oare ce sa fac? Sa aleg varianta 1 si sa innot pana la mal ori varianta 2 pur si simplu sa astept pana voi ajunge acolo?\n > Deci 1 sau 2? ")
      if choice3 == "1":
        print("Gandind ca un invingator, iti repeti in minte 'ACUM ORI NICIODATA!'")
        time.sleep(5)
        print("Fara sa stai pe ganduri sari peste bord!")
        time.sleep(5)
        print("Continui sa innoti catre insula si afara se intuneca si mai mult, acum este noapte.")
        time.sleep(5)
        print("Pare ca insula a disparut in intuneric, nestiind cat de departe esti de insula te ia panica!")
        time.sleep(5)
        print("Incerci sa innoti mai repede insa incepi sa obosesti!")
        time.sleep(5)
        print("Esti din ce in ce mai obosit si pare ca nu ai facut niciun progres, iar acum te afli intr-un intuneric total!")
        time.sleep(5)
        print("Incepi sa intri in panica si sa te gandesti daca nu ar fi fost mai bine doar sa astepti pe bordul navei...")
        time.sleep(5)
        print("Esti atat de obosit incat nu mai poti sa te misti si deodata te ia un carcel la maini si te paralizeaza!")
        time.sleep(5)
        print("Nu mai poti innota si te scufunzi sub apa...")
        time.sleep(5)
        print("Incerci sa iti tii respiratia cu speranta ca o sa iti revii si o sa poti innota spre suprafata...")
        time.sleep(5)
        print("Insa nu mai ai aer si deschizi gura sub apa...")
        time.sleep(5)
        print("Apa incepe sa iti inunde plamanii si te zbati fara scapare, totul se intuneca...")
        time.sleep(3)
        print("......")
        time.sleep(3)
        print("GAME OVER - Ai murit inecat.")
      elif choice3 == "2":
        print("Fiindca nu vrei sa iti complici viata decizi sa ramai pe vapor si sa astepti pana cand vei ajunge pe insula.")
        time.sleep(5)
        print("Intr-un final nava opreste in portul insulei...")
        print("Si te gandesti ca asta este momentul tau! Acum trebuie doar sa gasesci comoara!")
        time.sleep(7)
        print("Te strecori de pe barca pescarilor fara sa fii vazut de echipaj si fugi spre iesirea portului!")
        time.sleep(5)
        print("Din spate poti auzi un strigat de femeie:\n- STAI!")
        time.sleep(5)
        print("Pentru ca nu ai ajuns atat de departe ca sa fii oprit acum continui sa fugi dar...")
        time.sleep(5)
        print("Inevitabilul se intampla si piciorul tau drept este strapuns de o sageata!")
        time.sleep(5)
        print("Te lovesti de pamant si iti pierzi constiinta... cazand intr-un somn profund.......")
        time.sleep(2)
        print("...")
        time.sleep(4)
        print("......")
        time.sleep(2)
        print("!!!!!!!!!")
        time.sleep(2)
        print("Te trezesti legat fedeles, 2 femei imbracate in armura te taraie de picioare pe jos dupa ele.")
        time.sleep(5)
        print("Pentru ca esti legat la gura nu poti decat sa scoti sunete de protest!\nInsa pare ca nu esti bagat in seama si esti carat ca un sac de cartofi pe jos.")
        time.sleep(8)
        print("Ajungi intr-un canion unde poti vedea mai multe figuri de oameni... nemiscate...")
        time.sleep(5)
        print("Acei oameni erau morti... parea sa fie o vale a mortii.....")
        time.sleep(5)
        print("Si nu doar atat, toti oamenii ucisi in aceasta regiune erau strapunsi de o tepusa uriasa din lemn, lasati sa putrezeasca in soare!")
        time.sleep(8)
        print("Disperat incerci sa te zbati fiind orifiat de toti oamenii aceia trasi in teapa...")
        time.sleep(5)
        print("Te zbati in zadar pana cand cele 2 femei in armura te duc langa o tepusa din lemn goala...")
        time.sleep(5)
        print("Cele 2 femei te ridica in aer de parca ai fi un sac gol si te arunca in teapa!")
        time.sleep(5)
        print("Tepusa din lemn uriasa iti strapunge coloana vertebrala trecand prin tine si iesind prin abdomenul tau!")
        time.sleep(5)
        print("................")
        time.sleep(5)
        print("GAME OVER - Ai fost tras in teapa.")
  elif choice1 == "3":
    print("Decizi sa iti incerci norocul pe vaporul de transport marfa.")
    time.sleep(5)
    print("Te dai drept unul dintre muncitori si fara sa atragi nici-o privire acum esti pe nava.")
    time.sleep(5)
    print("Te afli deja pe ocean si de nicaieri un barbat burtos si pitic striga la tine:")
    time.sleep(5)
    print("- Ba sclavule! Nu-ti arde-a munca ei?")
    time.sleep(5)
    print("Intimidat acum de acel barbat te gandesti cum sa raspunzi...")
    print("- As putea sa il injur inapoi\n- Ori as putea sa ma supun, pare a fi un fel de sef pe aici")
    answer1 = input("Cum sa procedez mai departe?\n> Aleg varianta 1 sau 2?  ")
    if answer1 == "1":
      print("Pentru ca nu poti sa accepti fiind calcat in halul asta in picioare, ii raspunzi inapoi grasanului:")
      time.sleep(5)
      print("- Sclav e ma-ta ba!")
      time.sleep(5)
      print("Alt muncitor de pe nava te loveste pe la spate direct in cap cu o lopata.")
      time.sleep(5)
      print("Muncitorul spune:\n- Nu asa vorbesti cu seful jegule!")
      time.sleep(5)
      print("Iti pierzi constiinta si cazi in fata...")
      time.sleep(5)
      print("Te lovesti cu capul de marginea balustradei vaporului si iti rupi gatul...")
      time.sleep(5)
      print("GAME OVER - Ai murit cu gatul rupt.")
    elif answer1 == "2":
      print("Imi spun in minte 'Pentru a-mi atinge obiectivul trebuie sa fac sacrificii iar acesta este unul dintre ele.'")
      time.sleep(5)
      print("Asadar ii raspund inapoi burtosului:\n- Da sefu! Er.. adica... Nu.. nu chiulesc, doar luam o pauza de o tigara!")
      time.sleep(5)
      print("Grasanul raspunde:\n- Tigara ei? Mars la munca putoare!\n- Uite apuca o lopata de colo si dai la carbune, nava asta nu se pune singura in miscare!")
      time.sleep(5)
      print("Pentru ca am decis sa merg mai departe cu alegerea aceasta fac ce mi se spune si iau o lopata...")
      time.sleep(5)
      print("Muncind la carbune cu lopata impreuna cu alti muncitori brusc ma gandesc la a ma face nevazut cand nimeni nu se uita dupa mine.")
      time.sleep(5)
      print("Cu grija si cu atentie, fara sa par suspicios reusesc sa ma debarasez de restul muncitorilor si ma ascund dupa niste cutii pe puntea din fata a navei.")
      time.sleep(5)
      print("Nu trece mult si in zare se poate observa o insula!")
      time.sleep(5)
      print("Fara dar si poate aceasta trebuie sa fie insula amazoanelor!")
      time.sleep(5)
      print("Dar oare ce ar trebui sa fac?\n- Sa astept pana cand ancoreaza nava pe insula in siguranta\n- Sau sa iau una dintre barcile de salvare gonflabile si sa ma indrept singur catre insula")
      choice2 = input("> Oare ce varianta sa aleg? 1 sau 2?  ")
      if choice2 == "1":
        print("Pentru ca am fost un fricos toata viata mea, decid sa nu ma risc si astept ca vasul sa ancoreze pe insula.")
        time.sleep(5)
        print("In cele din urma vaporul cu marfa ancoreaza langa o barca cu pescari.")
        time.sleep(5)
        print("Entuziasmat ca ai ajuns pe insula cobori de pe vaporul cu marfa.")
        time.sleep(5)
        print("Esti vazut imediat de o femeie frumoasa in armura care striga la tine:\n- STAI!")
        time.sleep(5)
        print("Pentru a nu creea o situatie periculoasa faci ce zice si astepti ca femeia sa vina la tine.")
        time.sleep(5)
        print("Ajunsa in fata ta femeia iti vorbeste pe un ton autoritar:\n- Sclavii nu au ce cauta pe mal!")
        time.sleep(3)
        print("- Spune repede ce cauti aici ori te decapitez pe loc!")
        time.sleep(3)
        print("Fara alte avertismente amazoanca scoate o sabie din teaca si se pune in garda!")
        time.sleep(5)
        print("Obligat sa decizi rapid te gandesti doar la 2 variante:\n- As putea sa o mint\n- Sau as putea sa incerc sa o seduc")
        choice3 = input("> Ce varianta sa aleg? 1 sau 2?  ")
        if choice3 == "1":
          print("Incercand sa inventez un motiv deschid gura si spun:\n- Ah.. Pai aam... Seful meu mi-a cerut sa aduc ceva de aici.")
          time.sleep(5)
          print("- Si aam... da... de asta sunt aici.")
          time.sleep(5)
          print("Vezi doar o miscare rapida in timp ce auzi un urlet de femeie salbatic...")
          time.sleep(5)
          print("Privirea ti se inroseste in timp ce femeia nebuna iti spinteca capul de pe umeri dintr-o miscare!")
          time.sleep(5)
          print("GAME OVER - Ti-ai pierdut capul.")
        elif choice3 == "2":
          print("Gandindu-ma ca este o insula doar de femei razboinice decid sa o seduc pe amazoanca.")
          time.sleep(5)
          print("Cu un zambet jucaus pe buze ii spun femeii:\n- Buna frumoaso!")
          time.sleep(5)
          print("- Motivul pentru care sunt aici, desigur, esti tu!")
          time.sleep(5)
          print("- Si ...")
          time.sleep(5)
          print("Nu apuci sa iti termini propozitia ca dintr-o miscare rapida si un urlet feroce de femeie amazoanca iti spinteca capul de pe umeri!")
          time.sleep(5)
          print("Vezi doar rosu in fata in timp ce capul tau cade pe jos detasat de corp.")
          time.sleep(5)
          print("GAME OVER - Ti-ai pierdut capul.")
      elif choice2 == "2":
        print("Toata viata mea am fost independent si am luat cele mai calculate decizii.\nSi de data aceasta aleg sa iau o decizie calculata!")
        time.sleep(5)
        print("Merg la o barca de salvare si o arunc in apa iar la scurt timp sar in apa dupa ea si ma catar in barca gonflabila.")
        time.sleep(5)
        print("Cu o vasla vaslesc spre tarmul insulei")
        time.sleep(5)
        print("In cele din urma ajung pe insula si zaresc o cladire inalta ce pare a fi un palat.")
        time.sleep(5)
        print("Ma indrept spre cladirea inalta fiind sigur pe mine ca acolo se afla Diamantul Printesei!")
        time.sleep(5)
        print("Dar pe drum dau de un grup de femei frumoase in armura ce chicoteau si nu pareau sa ma observe.")
        print("Le evit sau le salut?")
        choice3 = input("> Aleg varianta 1 sau 2? ")
        if choice3 == "1":
          print("Fara sa stau pe ganduri, decid ca este mai sigur pentru mine sa nu atrag priviri asa ca le evit pe acele femei frumoase.")
          time.sleep(5)
          print("Ajung langa cladirea inalta si pot vedea intrarea care nu parea pazita!")
          print("Oare sa intru pe usa din fata sau sa caut o alta intrare?")
          choice4 = input("> Aleg varianta 1 sau 2?  ")
          if choice4 == "1":
            print("Decid sa intru pe usa din fata fiindca nu o pazea nimeni.")
            time.sleep(5)
            print("Acum ma aflu in interiorul palatului Printesei Eveline.")
            time.sleep(5)
            print("Pentru a nu pierde nici-un minut, incep sa caut Diamantul!")
            time.sleep(5)
            print("Din exteriorul castelului aud mai multe voci de femeie printre care:")
            time.sleep(5)
            print("- Avem un intrus! L-am vazut intrand pe usa principala!")
            time.sleep(5)
            print("Panicat de ce auzi, disperat cauti un loc in care sa te ascunzi si cand intorci privirea...")
            time.sleep(5)
            print("O sulita iti strapunge capul fix printre ochi!")
            time.sleep(5)
            print("Cazi mort la pamant intr-o balta de sange cu o sulita infipta in cap...")
            time.sleep(5)
            print("GAME OVER - Ai murit cu o sulita infipta in cap.")
          elif choice4 =="2":
            print("Ma gandesc sa fiu precaut si caut alta intrare in palat.")
            time.sleep(5)
            print("Gasesc un geam deschis in lateralul palatului si ma strecor inauntru.")
            time.sleep(5)
            print("Acum ma aflu in interiorul palatului Printesei Eveline.")
            time.sleep(5)
            print("Pentru a nu pierde nici-un minut incep sa caut Diamantul!")
            time.sleep(5)
            print("Dau peste o incapere eleganta, cu un pat matrimonial bine intretinut, tablouri pe pereti si miros de Lavanda.")
            time.sleep(5)
            print("Observ ca langa pat se aflau 2 noptiere iar pe una dintre ele era un obiect lung si gros aurit.")
            time.sleep(5)
            print("Ma apropii de obiectul aurit si realizez ca acesta trebuie sa fie Diamantul Printesei Eveline!")
            time.sleep(5)
            print("Insfac comoara si imi planific intoarcerea mea cand pe cealalta noptiera observ un cristal galben.")
            time.sleep(5)
            print("Langa cristal o lista de instructiuni.")
            choice5 = input("- Am oare timp sa vad instructiunile\n- Sau ar trebui sa fug?\n> Ce sa aleg varianta 1 sau 2?  ")
            if choice5 == "1":
              print("Pentru ca ar putea fi inca o comoara decid sa citesc instructiunile si sa vad ce poate face acel cristal.")
              time.sleep(5)
              print("Pe foaia scria:\nPentru a folosi in siguranta cristalul translocarii..\nPrima data gandeste-te la locatia unde vrei sa aterizezi si tine imaginea in minte..\nDupa care ia cristalul in mana..\nSi rosteste cuvantul PORTAL cu voce tare!")
              time.sleep(10)
              print("Citind cu atentie instructiunile realizez ca acesta ar putea fi biletul meu de scapare!")
              time.sleep(5)
              print("Asa cum am citit in instructiuni, mai intai m-am gandit la debarcaderul din care am pornit..")
              time.sleep(5)
              print("Dupa care am luat cristalul galben in mana...")
              time.sleep(5)
              print("Si cu voce tare am spus:\n- PORTAL!")
              time.sleep(5)
              print("Un bubuit urias ca de traznet se aude si vad alb in fata ochilor mei pentru cateva secunde..")
              time.sleep(5)
              print("....")
              time.sleep(5)
              print("Incep sa imi recapat vederea si realizez ca sunt din nou in portul din care am pornit insa toate vapoarele erau acum plecate")
              time.sleep(5)
              print("Verific buzunarul in care am ascuns comoara si vad un obiect lung si gros placat cu aur!")
              time.sleep(5)
              print("Am reusit sa fur Vibrtorul placat cu aur al Printesei Eveline!")
              time.sleep(5)
              print("Acum il voi vinde si ma voi imbogati!")
              print("AM REUSIT!")
            elif choice5 == "2":
              print("Fara sa stau prea mult pe ganduri decid ca nu am timp de prostii si ca ar trebui sa scap de pe insula cu comoara mea!")
              time.sleep(5)
              print("Ies grabit din camera Printesei cand din spate aud un vajait!")
              time.sleep(5)
              print("O sageata te strapunge din spate fix in coloana vertebrala si iese prin stomacul tau!")
              time.sleep(5)
              print("Auzi o femeie urland:\n- Avem un intrus!")
              time.sleep(5)
              print("In timp ce cazi in genunchi lipsit de putere, o a doua sageata te strapunge din spate,\nsi iese din pieptul tau trecand fix prin inima ta!")
              time.sleep(5)
              print("Fara nici-o putere ramasa si cu vederea intunecata, cazi la pamant in timp ce inima ta tocmai sa oprit!")
              time.sleep(5)
              print("GAME OVER - Ai murit cu 2 sageti infipte in tine.")
        elif choice3 == "2":
          print("Sedus de frumusetea acestor femei decid sa le abordez:")
          time.sleep(5)
          print("Cu un ranjet prostesc pe fata le salut:\n- Buna domnisoarelor!")
          time.sleep(5)
          print("Nu apuc sa scot alt cuvant ca aud mai multe urlete salbatice!")
          time.sleep(5)
          print("- ARRRRRGGGGGGG!")
          time.sleep(5)
          print("In mai multe miscari fulger esti trantit la pamant si batut brutal de acele femei in armura!")
          time.sleep(5)
          print("Una din femei te calca pe gat moment in care se aude o pocnitura si simti ca te sufoci!")
          time.sleep(5)
          print("In timp ce alta femeie iti rupe piciorul drept de la jumatatea tibiei!")
          time.sleep(5)
          print("Si alta femeie iti suceste mana stanga din umar!")
          time.sleep(5)
          print("Nu mai poti gandi limpete din cauza durerii si viziunea ti se incetoseaza!")
          time.sleep(5)
          print("Inainte sa iti pierzi constiinta se aud mai multe pocnituri de oase!")
          time.sleep(5)
          print("GAME OVER - Ai murit rupt in bataie.")
  else:
    print("Man, ti-am dat mur in gura, alegi 1, 2 sau 3? Incearca din nou.")

elif aventura == "nu":
  print("Bohohoo, nu ai coaie in pantaloni ha?\nAsa ma gandeam si eu, da-i drumu de aici, iti meriti mizeria de viata pe care o traiesti.")
else:
  print("Prietene e simplu, fa o alegere: da sau nu, ai tupeu sau nu?")