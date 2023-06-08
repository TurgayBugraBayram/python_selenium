# class car:
#     model = "toyota"
#     year = 2015
#
# araba1 = car()
# print(araba1.year)
# print(araba1.model)
# print(araba1)
# araba2 = car()
# print(araba2.year)
#
# print(car.year)
#
# print(dir(araba1))


# class araba:
#     def __init__(self, model = "bilgi yok", year ="bilgi yok"):
#         self.model = model
#         self.year = year
#
#
# araba1 = araba("toyota",2012)
# print(araba1.model)
# print(araba1.year)
#
# araba2 = araba("bmw",2020)
# print(araba2.model)
# print(araba2.year)
#
# araba3 = araba(year=1999)
# print(araba3.year)
# print(araba3.model)

# class yazılımcı:
#     def __init__(self,isim,soyisim,diller,maaş):
#         self.isim = isim
#         self.soyism = soyisim
#         self.diller = diller
#         self.maaş  = maaş
#
#     def showInfos(self):
#         print(f"""
#         İsim : {self.isim}
#         Soyisim : {self.soyism}
#         Diller : {self.diller}
#         Maaş : {self.maaş}
#         """)
#     def maaş_zam(self,zam_miktarını):
#         print("Zam yaplılıyor...")
#         # self.maaş = maaş+zam_miktarını
#         self.maaş += zam_miktarını
#
#     def dil_ekle(self,yeni_dil):
#         print("Yeni dil eklneiyor...")
#         self.diller.append(yeni_dil)
#
#     def __str__(self):
#         return "Bu bir yazılımcıların bulunduğu bir class"
#
#     def __del__(self):
#         print("İşten çıkarıldı")
#
# yazılımcı1 = yazılımcı("ahmet","mehmet",["python","java"],1000)
#
# yazılımcı1.showInfos()
# yazılımcı1.maaş_zam(250)
# yazılımcı1.dil_ekle("c")
# yazılımcı1.showInfos()
#
# print(dir(yazılımcı1))
# del yazılımcı1



class animal:
    name = ""
    def eat(self):
        print("yemek yedi")
    def sleep(self):
        print("uyudu")

class Dog(animal):
    def havlama(self):
        print("havladı")


dog1 =Dog()

dog1.eat()
dog1.havlama()

animal1 = animal()


class bilgisayar:
    def __init__(self):
        self.__max_fiyat =10000 #priveta
        self._abc= ""           #procted
        self.standat=1          #public

    def setFiyat(self,fiyat):
        self.__max_fiyat=fiyat

    def satma(self):
        print(f"Satıldı : {}")

bilgisayar1 = bilgisayar()

class Polygon:
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):

    def render(self):
        print("Rendering Circle...")

