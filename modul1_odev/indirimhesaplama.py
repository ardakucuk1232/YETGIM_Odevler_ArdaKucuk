fiyat = float(input("Ürün fiyatı: "))

indirim = float(input("İndirim yüzdesi: "))

if indirim > 0 and indirim < 100:
    indirimMiktari = fiyat * indirim / 100

    yeniFiyat = fiyat - indirimMiktari
    
    print("İndirim Miktarı: ", indirimMiktari)
    print("Yeni Fiyat: ", yeniFiyat)

else:
    print("İndirim yüzdesi 0-100 arası olmalı")