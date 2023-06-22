import selenium
# print(a)
# int("abc")
# 2/0
# print("abc"12)
# print("abc"+12)

# try:
#     a = int("abc")
#     print("try calısti")
# except ValueError:
#     print("except calıstı")
#
# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except ZeroDivisionError:
#     print("Bir sayı sıfıra bölünemez")
# except ValueError:
#     print("Dogru deger girin")
# except:
#     print("HATA")

# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except (ZeroDivisionError,ValueError):
#     print("Bir sayı sıfıra bölünemez ve Dogru deger girin")



# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except ZeroDivisionError:
#     print("Bir sayı sıfıra bölünemez")
# except ValueError:
#     print("Dogru deger girin")
# finally:
#     print("finally calıstı")
#

# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except ZeroDivisionError:
#     print("Bir sayı sıfıra bölünemez")
# except ValueError:
#     print("Dogru deger girin")
# else:
#     print("else calıstı")


def terscevir(kelime):
    if type(kelime) != str:
        raise ValueError("lütfen dogru deger girin")
    else:
        return kelime[::-1]

# print(terscevir("python"))
#
# print(terscevir(10))

try:
    print(terscevir(10))
except ValueError:
    print("func bir hata olustu")

from Ders5 import selam
import Ders5 as a
a.selam()

