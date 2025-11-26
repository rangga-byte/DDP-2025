def Lpersegi (sisi):
    return sisi * sisi


def Lsegitiga (alas, tinggi):
    return 0.5 * alas * tinggi


def Llingkaran (jari_jari):
    return 3.14 * jari_jari * jari_jari


def Ljajaran_genjang (alas, tinggi):
    return alas * tinggi


def Lpersegi_panjang (panjang, Lebar):
    return panjang * Lebar

print(Lpersegi_panjang(2,4))
print(Ljajaran_genjang(3,5))
print(Llingkaran(7))
print(Lsegitiga(4,6))
print(Lpersegi(4))

def Kpersegi (sisi):
    return 4 * sisi

def Ksegitiga (sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def Klingkaran (jari_jari):
    return 2 * 3.14 * jari_jari

def Kjajaran_genjang (sisi1, sisi2):
    return 2 * (sisi1 + sisi2)

def Kpersegi_panjang (panjang, Lebar):
    return 2 * (panjang+Lebar)
                
print(Kpersegi_panjang(2,4))
print(Kjajaran_genjang(3,5))
print(Klingkaran(7))
print(Ksegitiga(4,6,2))
print(Kpersegi(4))