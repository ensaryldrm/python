sepet = []
print("Çıkmak için 'q' tuşuna basınız")
while True:
    urun = input("Sepete eklemek istediğiniz ürünü giriniz: ")
    if urun == "q":
        break
    sepet.append(urun)
print(f"Sepetteki ürünler {sepet}")
