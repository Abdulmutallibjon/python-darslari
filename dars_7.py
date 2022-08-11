# 10 IF-ELSE
# if OPERATORI
avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:  # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper())  # avto nomini hamma harflarini katta bilan yoz.
    else:  # aks holda ...
        print(avto.title())  # avto nomini faqat birinchi harfini katta bilann yoz.

# Diqqat! Shart "badani" shartdan biroz o'ngga surib yoziladi
# (huddi for tsikli kabi). if/else dan keyin kelgan va
# o'ngga surib yozilgan har bir qator if/else shartining badani hisoblanadi.

# TRUE/FALSE
ism = "ali"
if ism == "Ali":
    print(ism)
else:
    print(ism)

# QIYMATLARNING TENG EMASLIGINI TEKSHIRISH
ism = input('Ismingiz nima?\n>>>')  # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali':  # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.")  # quyidagi xabar chiqadi
else:
    print("Salom, Ali")

# SONLARNI SOLISHTIRISH
javob = float(input("12x6 nechiga teng?>>>"))
if javob != 72:
    print("Javob xato!")

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh >= 18:  # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else:  # ask holda
    print('Kirish mumkin emas!')

# BIR QATOR if/else
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh > 65: print("Siz COVID-19 risk guruhida ekansiz")
# yoki
x, y = 25, 50  # x=25 va y=50
print("x>y") if x > y else print("x<y")
