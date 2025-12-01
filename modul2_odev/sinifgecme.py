vize = float(input("Vize notu: "))
final = float(input("Final notu: "))

ort = (vize * 0.4) + (final * 0.6)

if ort >= 90:
    print("Harf notu: AA")

elif ort >= 80:
    print("Harf notu: BA")

elif ort >= 70:
    print("Harf notu: BB")

elif ort >= 60:
    print("Harf notu: CB")

elif ort >= 50:
    print("Harf notu: CC")

else:
    print("Kaldın Harf notu: FF")