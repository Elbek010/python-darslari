# 1- misol
# def n_ni_hisobla(son):
#     if son == 0:
#         return 0
#     else:
#         return n_ni_hisobla(son-1)*son
# print(n_ni_hisobla(23))
# 2 - misol
# def fibalanchi_son(n):
#     if n == 1 or n ==2:
#         return 1
#     else:
#         return fibalanchi_son(n - 1) + fibalanchi_son(n - 2)
# print(fibalanchi_son(23))
# 3 - misol
# def raqam_yegindisi(n):
#     if n<10:
#         return n
#     else:
#         return n%10 + raqam_yegindisi(n//10)
# print(raqam_yegindisi(30))
# 4 - misol
# def ohirgi_raqamni_top(n):
#     if n < 10:
#         return n
#     else:
#         return n%10
# print(ohirgi_raqamni_top(10))
# 5 - misol
# def raqamlar_soni(n):
#     if n == 0:
#         return 0 
#     else:
#         return 1 + raqamlar_soni(n//10)
# print(raqamlar_soni(789))
# 6 - misol
# def teskari_satr(matn):
#     if matn == "":
#         return "" 
#     else:
#         return matn [-1] + teskari_satr(matn[:-1])
# print(teskari_satr("qonday"))
# 7 - mispl
# def 

# 8 - misol
# def yigindi_royhat(sonlar):
#     if len(sonlar) == 0:
#         return 0
#     else:
#         return sonlar[0] + yigindi_royhat(sonlar[1:])
# print(yigindi_royhat([10,20,30]))

# a = int(input("son kiriting:")) 
# b = int(input("son kiriting:"))
# c = int(input("son kiriting:"))
# d = a+b+c
# print(d)

# 9 - misol
# def eng_katta_son(son):
#     if len(son)== 0:
#         return 0
#     else:
#         return 
# print(eng_katta_son([10,20,30]))
# 11 - misol
# def darajada_AvaB(a,b):
#     if b == 0:
#         return 1
#     else:
#         return a * darajada_AvaB(a, b - 1)
# print(darajada_AvaB(2,3))
# 12 - misol
# def EKUB(a, b):
#     if b == 0:
#         return a
#     else:
#         return EKUB(b, a % b)
# print(EKUB(48,18))
# 13 - misol
