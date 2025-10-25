# 1 - misol

# def foydalanuvchi_ismi(ism):
#     if ism == ism:
#         return (f"salom " + ism)
#     else:
#         return "katak bo'sh"
# print(foydalanuvchi_ismi("elbek"))
# 2 - misol
# def kvadrat_ikki(son):
#     if son == 2:
#         return son**2
#     else:
#         return "siz boshqa sonni kiritdingiz"
# print(kvadrat_ikki(2))
# 3 - misol
# def kvadrat(a, b):
#         return (a **2) and (b **2)
# print(kvadrat(10,30))
# 4 - misol
# def sonlar_yegindisi(sonlar):
#         if len(sonlar) == 0:
#                 return 0
#         else:
#                 return sonlar[0] + sonlar_yegindisi(sonlar[1:])

# print(sonlar_yegindisi([10,20,30,40]))
# # 5 - misol
# sozlar = []
# def  unli_soz_borligini_aniqla(sozlar):
#     if sozlar in "aoueo'AOUEO'" :
#         return unli_soz_borligini_aniqla([])
#     else:
#         return sozlar
# print(unli_soz_borligini_aniqla("salom"))


kvadrat = lambda a,b : a**b
print(kvadrat(10,2))