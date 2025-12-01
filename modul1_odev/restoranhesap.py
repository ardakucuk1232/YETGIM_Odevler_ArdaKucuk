yemek = float(input("Yemek fiyatı: "))
bahsis = float(input("Bahşiş yüzdesi: "))
kisi = int(input("Kişi sayısı: "))

if bahsis >= 0 and kisi > 0:
    bahsisMiktar = yemek * bahsis / 100
    toplam = yemek + bahsisMiktar
    kisiBasi = toplam / kisi

    print("Bahşiş:", bahsisMiktar)
    print("Toplam Tutar:", toplam)
    print("Kişi Başı:", kisiBasi)

else:
    print("Kişi veya bahşiş hatalı")