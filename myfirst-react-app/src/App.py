ad_soyad=input("Ad�n�z-Soyad�n�z: ")
yabanci_dil=input("Bildi�iniz yabanc� dil: ")
yas=int(input("Ya��n�z: "))
 
if ((yabanci_dil=="�ngilizce" or yabanci_dil=="Frans�zca" or yabanci_dil=="�talyanca" and yabanci_dil=="T�rk�e") and yas<50):
    print("Kriterlere uydu�unuz i�in i�e al�n�dn�z")
else:
    print("Kriterlere uyamad���n�z i�in i�e al�nmad�n�z")