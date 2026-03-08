while True:
    mesaj = input("Bir şey yazın (Çıkmak için 'q' tuşuna basın): ")
    
    if mesaj == "q":
        print("Sistem kapanıyor...")
        break # Bu komut çalıştığında döngü tamamen durur.
        
    print(f"Yazdığınız mesaj: {mesaj}")