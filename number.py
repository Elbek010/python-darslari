# def juft_yoki_toqligini_aniqlash(son):
#     if son % 2 == 0:
#         print("Bu son juft")
#     else:
#         print("Bu son toq")
# juft_yoki_toqligini_aniqlash(4)
# royhat = [10, 20, 39, 41, 5, 6, 17, 8, 90]
# def hisoblash(royhat):
#     for i in range(2):
#         juft_yoki_toqligini_aniqlash(royhat[i])
#             print(f"{royhat[i]} soni juft")
#         else:
#             print(f"{royhat[i]} soni toq")
# hisoblash(royhat)



# def juft_yoki_toqligini_aniqlash(son):
#     if son % 2 == 0:
#         print("Bu son juft")
#     else:
#         print("Bu son toq")
#         return son
# juft_yoki_toqligini_aniqlash(5)



# def musbat_yoki_manfiy(son):
#     if son > 0:
#         print("Bu son musbat")
#     else:
#         print("Bu son manfiy")
#         return son
# musbat_yoki_manfiy(-5)
# royhat = [10, 20, 39, 41, 5, 6, 17, 8, 90]


# def ortacha_qiymatni_hisobla(royhat):
#     yigindi = sum(royhat)
#     soni = len(royhat)
#     ortacha = yigindi / soni
#     return ortacha 
# print(ortacha_qiymatni_hisobla([10, 20, 40, 40, 10]))
# print(ortacha_qiymatni_hisobla([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 22
# def takrorlanuvchi_elementlarni_ochir(royhat):
#     yangi_royhat = []
#     for element in royhat:
#         if element not in yangi_royhat:
#             yangi_royhat.append(element)
#     return yangi_royhat
# print(takrorlanuvchi_elementlarni_ochir([1,2,3,3,4,5,5,6,7,8,8,9,10]))
# print(takrorlanuvchi_elementlarni_ochir([10, 20, 20, 30, 40, 40, 50]))

# def yigindini_hisobla(royhat):
#     yigindi = sum(royhat)
#     return yigindi
# print(yigindini_hisobla([1, 2, 3, 4, 5]))
# print(yigindini_hisobla([10, 20, 30, 40, 50]))

# 23
# def royhatni_teskari_qilish(royhat):
#     yangi_royhat = royhat[::-1]
#     return yangi_royhat
# print(royhatni_teskari_qilish([1,2,3,4,5,6,7,8,9,10]))
# print(royhatni_teskari_qilish([10,20,30,40,50,90,80,70,60]))


# def kopaytmani_hisobla(royhat):
#     kopaytma = 1
#     for son in royhat:
#         kopaytma *= son
#     return kopaytma
# print(kopaytmani_hisobla([1,2,3,4,5]))
# print(kopaytmani_hisobla([10,20,30]))

# 24

# def tubligini_aniqlash(son):
#     if son < 2:
#         return False
#     for i in range(2, int(son**0.5) + 1):
#         if son % i == 0:
#             return False
#     return True
# print(tubligini_aniqlash(11))
# print(tubligini_aniqlash(15))
# 25
# def tubligini_aniqlash(son):
#     tublar = []
#     murakkablar = []

#     for n in range(2,son + 1):
#         tubmi = True
#         for m in range(2, int(n ** 0.5) + 1):
#             if n % m == 0:
#                 tubmi = False
#                 break
#             if tubmi :
#                 tublar.append(n)
#             else:
#                 murakkablar.append(n)

#     return tublar , murakkablar
# print(tubligini_aniqlash(20))
# 28
# def fitobalinchi(son):
#     a , b = 0,1
#     for i in range(son):
#         print(a , end= " ")
#         a, b = b, a + b
# fitobalinchi(10)
# 33
# def undosh_harflarni_olib_tashla(matn):
#     unli_harflar = "aeiouAEIOU"
#     natija = []
#     for harf in matn:
#         if harf not in unli_harflar:
#             natija += harf
#     return natija
# print(undosh_harflarni_olib_tashla("na gap javohir"))
# 34

# def bosh_harfni_kattalashtir(matn):
#     katta = ""
#     for harf in matn:
#         if matn.istitle:
#             katta += matn
#     return katta
# bosh_harfni_kattalashtir("salom")
# 35
# def raqam_yegindini_hisolash(son):
#     raqam = 0
#     for i in range(son + 1):
#         raqam += i
#     return raqam
# print(raqam_yegindini_hisolash(10))
# 36
# def raqam_kopaytmasini_hisoblash(sonlar):
#         raqam = str(sonlar)
#         kopaytma = 1  
#         for i in raqam:
#             kopaytma *=int(i)
#         return kopaytma
# print(raqam_kopaytmasini_hisoblash(12))

# 37 
# def palindromligini_hisobla(son):
#     raqam = str(son)
#     if son%11==0 or str(son) == raqam[::-1]:
#         return "palindrom"
#     else:
#         return "palindrum emas"
# print(palindromligini_hisobla(55))

# 38
def 












    