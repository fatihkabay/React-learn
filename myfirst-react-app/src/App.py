ad_soyad=input("Adýnýz-Soyadýnýz: ")
yabanci_dil=input("Bildiðiniz yabancý dil: ")
yas=int(input("Yaþýnýz: "))
 
if ((yabanci_dil=="Ýngilizce" or yabanci_dil=="Fransýzca" or yabanci_dil=="Ýtalyanca" and yabanci_dil=="Türkçe") and yas<50):
    print("Kriterlere uyduðunuz için iþe alýnýdnýz")
else:
    print("Kriterlere uyamadýðýnýz için iþe alýnmadýnýz")