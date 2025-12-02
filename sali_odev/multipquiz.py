import random

dogru = 0
yanlis = 0

for i in range(5):
    sayi1 = random.randint(1, 10)
    sayi2 = random.randint(1, 10)

    cevap = int(input(f"{sayi1} x {sayi2} = "))

    if cevap == sayi1 * sayi2:
        print("Doğru")
        dogru += 1
    else:
        print("Yanlış")
        yanlis += 1

print("Doğru sayısı:", dogru)
print("Yanlış sayısı:", yanlis)