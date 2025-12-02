print("1-) Üçgen, 2-) Dik Üçgen, 3-) Kare")

secim = int(input("Seçiminiz: "))

a = int(input("Boyut: ")) #satır sayısı

if secim == 1:
    for i in range(1, a + 1):
        print(" " * (a - i) + "*" * (2 * i - 1))

elif secim == 2:
    for i in range(1, a + 1):
        print("*" * i)


elif secim == 3:
    for i in range(a):
        print("*" * a)

else:
    print("1 ile 3 arasında seçim yapınız")