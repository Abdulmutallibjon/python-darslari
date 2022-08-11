# SONLAR
# int() - INTEGERS — BUTUN SONLAR
int(1_2_3_4_5)

# float() -  floating point numbers - O'NLIK SONLAR
float(1.01)

# UZUN SONLARNI KIRITISH
int(1232_232_323_4_5)   # raqamlarni pastki chiziq (_) yordamida guruhlash mumkin

# KONSTANTA
PI = 3.14159    # o`zgaruvchi katta harflar bilan yoziladi (ogohlantirish sifatida)

# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
x, y, z = 10, -7.25, -30

# O'ZGARUVCHI TURINI ALMASHTIRISH - typecasting detiladi
ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' yoshda'   # int => str ga almashtirildi
print(xabar)

# O'ZGARUVCHI TURINI TEKSHIRISH - type()
ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh))   # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz

# INPUT() VA SONLAR
# 1 foydalanuvchining tug'ilgan yilini so'raymiz va qiymatni int ga aylantiramiz
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# 2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil
# 3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")

# yoki int ni input ajratib yozish mumkin
# 1.1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = input("Tug'ilgan yilingizni kiriting: ")
# 1.2 t_yil o'zgaruvchini int ga aylantiramiz
t_yil = int(t_yil)
# 2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil
# 3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")
