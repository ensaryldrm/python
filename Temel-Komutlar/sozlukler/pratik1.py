odalar = {}


print("Çıkmak için 'q' tuşuna basınız!")
print("Yeni kayıt için '1' tuşuna basınız.")
while True:
    secim = input("Seçim: ")
    if secim == "q":
        break
    elif secim == "1":
        isim = input("İsminizi giriniz: ")
        oda_no = input("Oda numarası giriniz: ")
        odalar[oda_no] = isim
    else:
        print("Yanlış seçim yaptınız!")

for oda_no,isim in odalar.items():
    print(f"İsim: {isim}, oda no: {oda_no}")