# def selamla():
#     print("python selenium")
#     print("selamlar")
#
# selamla("merhaba")

# def selamla(isim,soyisim):
#     print(f"Merhaba {isim} {soyisim}")
#
# selamla(12,"abc")
#
#
# def toplama(a,b,c):
#     print(f"Toplamları {a+b+c}")
#
# toplama(1,2,3)
# toplama(52,40,1)

# def faktoriyel(sayı):
#     faktoriyel = 1
#     sayı_temp = sayı
#     if (sayı == 0 or sayı == 1):
#         print(f"{sayı}! = {faktoriyel}")
#     else:
#         while sayı > 1:
#             faktoriyel *=sayı
#             # faktoriyel = faktoriyel*sayı
#             sayı-=1
#         print(f"{sayı_temp}! = {faktoriyel}")
#
# faktoriyel(5)
# faktoriyel(3)

# def selamla(isim = "İsimsiz"):
#     print(f"Merhaba {isim}")
#
# selamla("bugra")

# def toplama(*sayılar):
#     toplam = 0
#     print("Paramatreler" , sayılar)
#     for i in sayılar:
#         toplam+=i
#     print(toplam)
#
# toplam = toplama(1,2,3)
# print(toplam)


# def toplam (a,b,c):
#     # print(a+b+c)
#     return a+b+c
# def ikicarp(a):
#     return a*2
#
# toplam1 = toplam(1,2,3)
# print(ikicarp(toplam1))

# iki_carp = lambda x: x * 2
#
# print(iki_carp(4))
#
# ciftek = lambda sayı: print("cift") if (sayı % 2) ==( 0) else print("tek")
# sayı = int(input("Bir sayı giriniz"))
# ciftek(sayı)

def myFunc(x):
    return lambda y : x*y

z = myFunc(5)
print(z)
print(z(4))
