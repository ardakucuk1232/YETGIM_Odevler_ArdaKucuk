ana_para = float(input("Ana para: "))
oran = float(input("Faiz oranı: "))
yil = int(input("Kaç yıl: "))

toplam = ana_para

for i in range(1, yil + 1):
    faiz = toplam * oran / 100
    toplam += faiz
    print(f"{i}. yıl toplam: {toplam:.2f}  |  Eklenen faiz: {faiz:.2f}")