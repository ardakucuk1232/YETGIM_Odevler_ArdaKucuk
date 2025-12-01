print("Doğum Tarihi:")

g = int(input("Gün: "))
a = int(input("Ay: "))
y = int(input("Yıl: "))

print("Bugünün Tarihi:")

gb = int(input("Gün: "))
ab = int(input("Ay: "))
yb = int(input("Yıl: "))

dogumToplam = y * 365 + a * 30 + g
bugunToplam = yb * 365 + ab * 30 + gb

if bugunToplam > dogumToplam:
    sonuc = bugunToplam - dogumToplam
    print("Bugüne kadar", sonuc, "gün yaşandı.")

else:
    print("Dogru tarih giriniz.")