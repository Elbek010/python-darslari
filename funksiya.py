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
def raqamlar_soni(n):
    if n == 0:
        return 0 
    else:
        return 1 + raqamlar_soni(n//10)
print(raqamlar_soni(789))
# 6 - misol
# def teskari_satr(matn):
#     if matn == "":
#         return "" 
#     else:
#         return matn [-1] + teskari_satr(matn[:-1])
# print(teskari_satr("qonday"))

      