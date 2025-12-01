print("Basit Dönüştürücü")
print("1 - Metre -> Feet || 2 - Feet -> Metre || 3 - Kilogram -> Pound || 4 - Pound -> Kilogram")

tip = input("Yapmak istediğiniz işlemi seçiniz 1 ile 4 arasında: ")

deger = float(input("Dönüştürmek istediğiniz değeri giriniz: "))

match tip:
    case "1": # metre to feet
        sonuc = deger * 3.28
        print(f"{deger} metre = {sonuc} feet")

    case "2": # feet to metre
        sonuc = deger / 3.28
        print(f"{deger} feet = {sonuc} metre")

    case "3": # kilogram to pound
        sonuc = deger * 2.2
        print(f"{deger} kilogram = {sonuc} pound")

    case "4": # pound to kilogram
        sonuc = deger / 2.2
        print(f"{deger} pound = {sonuc} kilogram")