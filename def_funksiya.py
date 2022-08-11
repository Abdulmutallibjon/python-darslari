# def yil_hisobla(ism, yosh):
#     """Foydalanuvchining yilini hisoblovchi funsiya"""
#     print(f"Foydalanuvchining ismi: {ism.title()}\n"
#           f"Foydalanuvchining yoshi: {yosh}\n"
#           f"Foydalanuvchining tug`ilgan yili: {2022-yosh}")
#
# yil_hisobla("ali", 28)
# def oraliq(min,max,qadam):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         if qadam:
#             tashla = min<max and qadam<max
#             min += qadam
#         else:
#             min += 1
#     return sonlar

# print(oraliq(0,10))
# print(range(0,10))
def oraliq(max, min=-1, qadam=1):
    sonlar = []
    while min < max:
        min += qadam
        sonlar.append(min)
        if max == len(sonlar):
           break
    return sonlar

print(oraliq(5,21,3))
