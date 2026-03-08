yas = int(input("Yaşınızı giriniz: "))
if yas >= 18:
    print(f"Yaşınız: {yas}, Tam bilet parası veriniz!")
elif yas >= 7:
    print(f"Yaşınız: {yas}, Öğrenci bilet parası veriniz!")
else:
    print(f"Yaşınız: {yas}, Çocuklar için bilet ücretsizdir!")