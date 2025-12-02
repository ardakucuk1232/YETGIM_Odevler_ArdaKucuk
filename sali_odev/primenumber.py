baslangic = int(input("Başlangıç sayısı: "))
bitis = int(input("Bitiş sayısı: "))

print("Asal Sayılar:")

for num in range(baslangic, bitis + 1):
    if num > 1:
        asal = True
        for i in range(2, num):
            if (num % i) == 0:
                asal = False
                break
        
        if asal:
            print(num)