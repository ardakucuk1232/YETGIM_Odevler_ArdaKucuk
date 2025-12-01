print("1 - Tavuk Döner (90 TL), 2 - Lahmacun (60 TL), 3 - Ayran (15 TL)")

tip = input("Seçiminiz: ")

match tip:
    case "1":
        toplam = 90
        print("Toplam:", toplam, "TL")

    case "2":
        toplam = 60
        print("Toplam:", toplam, "TL")

    case "3":
        toplam = 15
        print("Toplam:", toplam, "TL")
        
    case "1-3":
        toplam = 90 + 15
        print("Toplam:", toplam, "TL")
    
    case "2-3":
        toplam = 60 + 15
        print("Toplam:", toplam, "TL")