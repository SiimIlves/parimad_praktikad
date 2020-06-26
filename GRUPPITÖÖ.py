def nimekiri_lugudest():
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    albumid = []
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t')
        artist = rida_elementide_kaupa[0]
        album = rida_elementide_kaupa[1]
        albumid.append(album)
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("-------------------------------------------")
                print()
        print(rida)
    fail.close()
    
# JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON

def kõik_albumid():
    fail1 = open("a.txt", "w", encoding='utf-8')
    fail2 = open("albumid.txt", encoding='utf-8', errors ='ignore')
    for rida in fail2:
        rida_element = rida.split('\t')
        fail1.write(rida_element[0] + " - " + rida_element[1] + '\n')
    fail1.close()
    kõikalbumid()
def kõikalbumid():
    import os
    lines_seen = set()
    outfile = open("b.txt", "w")
    for line in open("a.txt", "r"):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    f = open("b.txt", "r", encoding='utf-8').read()
    print(f)
    os.remove("a.txt")
    os.remove("b.txt")
    
# JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON

# edasi teeme otsingu
def otsing_albumid(otsitav_album):
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    albumid = []
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t')
        artist = rida_elementide_kaupa[0]
        album = rida_elementide_kaupa[1]
        albumid.append(album)
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        '''
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("-------------------------------------------")
                print()
                '''
        if(album == otsitav_album):
            print(rida)
    fail.close()

# menüü kasutajale
print("1 - kõik albumid ja lood albumite kaupa")
print("2 - kõik albumid")
print("3 - albumi otsing")
print("4 - lugude otsing")
print()
valik = int(input("Sisesta oma valik: "))
if(valik == 1):
    nimekiri_lugudest()
if(valik == 2):
    kõik_albumid()
if(valik == 3):
    otsitav_album = input("Millist albumit otsid: ")
    otsing_albumid(otsitav_album)
