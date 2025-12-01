gelir = float(input("Gelirin: "))

if gelir <= 10000:
    vergi = gelir * 0.05

elif gelir <= 30000:
    vergi = gelir * 0.10

elif gelir <= 60000:
    vergi = gelir * 0.20

else:
    vergi = gelir * 0.30

net = gelir - vergi

print(f"Vergi miktarı: {vergi}")
print(f"Vergi sonrası net gelir: {net}")