#BÖLÜM1#

sayi1 = int(input("1.sayıyı giriniz: "))
print(f"1.sayı :{sayi1}")
sayi2 = int(input("2.sayıyı giriniz: "))
print(f"2.sayı :{sayi2}")

toplam = sayi1 + sayi2
print(f"Toplamları: {toplam}")
cıkarma= sayi1 - sayi2
print(f"Farkları: {cıkarma}")
carpma = sayi1 * sayi2
print(f"Çarpımları: {carpma}")
bolme = sayi1/sayi2
print(f"Bölüm: {bolme}")
mod = sayi1 % sayi2
print(f"Modu: {mod}")
üs= sayi1**sayi2
print (f"üssü: {üs}")


#BÖLÜM2#
print(f"GÖREV2")
sayi3=int(input("1 sayı giriniz: "))

toplam=0
for i in range(1, sayi3+1):
    toplam +=i

print(f"1'den {sayi3}'ya kadar olan sayıların toplamı: {toplam}")

print(f"GÖREV3")

for i in range(2, 100, 2 ):
    print(i, end=',')
print(f"\nGÖREV4")

metin = input("Bir metin girin: ")

ters_metin = ""

for harf in metin:
    ters_metin = harf + ters_metin  

print("Ters çevrilmiş metin:", ters_metin)
