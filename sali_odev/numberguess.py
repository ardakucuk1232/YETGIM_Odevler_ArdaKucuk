import random

min_sayi = 1
max_sayi = 100
rastgele = random.randint(min_sayi, max_sayi)
puan = 100

while True:
    guess = int(input("Tahminin: "))

    if guess == rastgele:
        print("Doğru bildin")
        puan += 10
        print("Puanın:", puan)
        break

    elif guess != rastgele:
        print("Yanlış bildin")
        puan -= 10
        print("Puanın:", puan)

    elif guess < rastgele:
        print("Daha büyük bir sayı dene")

    else:
        print("Daha küçük bir sayı dene")

    if puan == 0:
        print("Puanın bitti. Kaybettin")
        break