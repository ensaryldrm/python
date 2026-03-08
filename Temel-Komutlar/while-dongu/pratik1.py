while True: 
    girdi = input("Paket ağırlığı giriniz (Çıkmak için 'q' tuşuna basınız):")
    if girdi == "q":
        print("Sistemden çıkılıyor...")
        exit()
    
    sayi = int(girdi)
    if sayi <= 0:
        print("Yanlış değer girdiniz!")
    elif sayi <=5:
        print("Kargo ücreti 50TL")
    elif sayi <= 15:
        print("Kargo ücreti 150TL")
    else:
        print("Kargo ücreti 200TL")