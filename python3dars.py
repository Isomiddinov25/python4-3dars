
import os 
os.system("cls")

# # 20
# def ong_qoshnisi_kichik_sonlar(sonlar):
#     kichik_sonlar = []
#     for i in range(len(sonlar) - 1):
#         if sonlar[i] > sonlar[i + 1]:
#             kichik_sonlar.append(sonlar[i])
#     return kichik_sonlar, len(kichik_sonlar)


# n = 5
# sonlar = [10, 5, 8, 3, 7]

# kichik_sonlar, soni = ong_qoshnisi_kichik_sonlar(sonlar)
# print("O'ng qo'shnisi kichik bo'lgan sonlar:", kichik_sonlar)
# print("Bunday sonlar soni:", soni)
# # 21
# def osish_tartibida(sonlar):
#     return all(sonlar[i] <= sonlar[i + 1] for i in range(len(sonlar) - 1))
# n = 5
# sonlar = [1.1, 2.2, 3.3, 4.4, 5.5]

# natija = osish_tartibida(sonlar)
# print(natija)
# # 22  
# def kamayish_tartibida(sonlar):
#     for i in range(len(sonlar) - 1):
#         if sonlar[i] < sonlar[i + 1]:
#             return sonlar[i]
#     return 0

# n = 5
# sonlar = [5.5, 4.4, 3.3, 2.2, 1.1]

# natija = kamayish_tartibida(sonlar)
# print(natija)  
# # 23 da masala shartini sonlar arra shaklida bo'lsa degan joyini tushunmadim manimcha hato ketgan
# # # 24
# def oxirgi_2_nol_orasidagi_yigindi(sonlar):
#     oxirgi_2ta_nol_indeksi = [i for i, son in enumerate(sonlar) if son == 0][-2:]

    
#     if len(oxirgi_2ta_nol_indeksi) == 2:
#         start, end = oxirgi_2ta_nol_indeksi
#         yigindi = sum(sonlar[start + 1:end])
#         return yigindi
#     else:
#         return None  

# n = 10
# sonlar = [3, 0, 2, 4, 0, 1, 0, 5, 0, 7]

# natija = oxirgi_2_nol_orasidagi_yigindi(sonlar)
# print(natija) 
# # 25
# def birinchi_va_oxirgi_nol_orasidagi_yigindi(sonlar):
#     birinchi_nol_indeksi = sonlar.index(0)
#     oxirgi_nol_indeksi = len(sonlar) - 1 - sonlar[::-1].index(0)

#     yigindi = sum(sonlar[birinchi_nol_indeksi + 1:oxirgi_nol_indeksi])
#     return yigindi


# n = 10
# sonlar = [3, 0, 2, 4, 0, 1, 6, 5, 0, 7]

# natija = birinchi_va_oxirgi_nol_orasidagi_yigindi(sonlar)
# print(natija) 
# # 26 
# def darajaga_oshirish(sonlar,k):
#     natija = [son**k for son in sonlar]
#     return natija
# n = 4 
# k = 3 
# sonlar = [1.0, 2.5, 3.1, 4.0]
# natija =darajaga_oshirish(sonlar,k)
# print(natija)
# # 27
# def darajalarni_hisoblash(sonlar):
    
#     natijalar = [son ** (i + 1) for i, son in enumerate(sonlar)]
#     return natijalar


# n = 4
# sonlar = [1.0, 2.5, 3.1, 4.0]

# natijalar = darajalarni_hisoblash(sonlar)
# print(natijalar)  
# # 29
# def barcha_sonlar_yigindisi(toplamlar):
#     yigindi = 0
#     for toplam in toplamlar:
#         yigindi+=sum(toplam)
#         return yigindi
# n = 3 
# k = 2
# toplamlar = [ [1, 2, 3], [4, 5, 6] ] 
# natija = barcha_sonlar_yigindisi(toplamlar) 
# print(natija)
# 28
# def darajalarni_hisoblash(sonlar):
#     n = len(sonlar)
#     natijalar = [son ** (n - i) for i, son in enumerate(sonlar)]
#     return natijalar

# n = 4
# sonlar = [2.0, 3.0, 4.0, 5.0]

# natijalar = darajalarni_hisoblash(sonlar)
# print(natijalar)  


