# 'anahtar': 'değer' formatında yazılır.
kullanici = {
    "isim": "Ensar",
    "meslek": "Yazılım",
    "yas": 21
}

# Sözlükten bir veri çekmek için sırasını değil, anahtarın adını kullanırız.
print(kullanici["meslek"])  # Çıktı: Yazılım

# Boş bir sözlük oluşturma
sistem = {}

# Sözlüğe yeni bir kayıt ekleme
sistem["kullanici_adi"] = "admin123"

# Var olan bir kaydı güncelleme
sistem["kullanici_adi"] = "superadmin"