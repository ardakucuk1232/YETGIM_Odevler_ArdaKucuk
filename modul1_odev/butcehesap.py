print("Kişisel Bütçe Hesaplayıcı")

gelir = int(input("Gelirinizi giriniz: "))
gider = int(input("Giderinizi giriniz: "))

if gelir > gider:
    kalan = gelir - gider
    print(f"Kalan: {kalan} TL")

elif gelir < gider:
    kalan = gider - gelir
    print(f"Ekside kalan para: {kalan} TL")

else:
    print("Kalan 0 TL")

