# 11 BIR NECHTA SHARTLARNI TEKSHIRISH
# if-elif-else KETMA-KETLIGI

# TODO Diqqat! if-elif-else ketma-ketlikda biror shart
#  bajarilishi bilan, Python qolgan shartlarni tekshirmaydi.

yosh = int(input('Yoshingiz nechida? '))
if yosh <= 4:
    print('Sizga kirish bepul.')
elif yosh <= 12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')

# TODO Kod yozishda yaxshi amaliyotlardan biri, kodlarni
#  qisqa yozish va buyruqlarni qayta-qayta takrorlamaslik.
#  Bu kelajakda kodni o'zgartirishda ham juda qo'l keladi.

yosh = int(input('Yoshingiz nechida? '))
if yosh <= 4:
    price = 0
elif yosh <= 12:
    price = 5000
else:
    price = 10000

print(f"Sizga kirish {price} so'm")

# hayvonot bog'i qariyalar uchun chegirma e'lon qilsa,
# kodimizni quyidagicha o'zgartirishimiz mumkin

yosh = int(input('Yoshingiz nechida? '))
if yosh <= 4:  # yosh bolalarga bepul
    price = 0
elif yosh <= 12:  # 4 dan 12 yoshgacha 5000 so'm
    price = 5000
elif yosh < 65:  # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
    price = 10000
else:  # qariyalarga esa 8000 so'm
    price = 8000
print(f"Sizga kirish {price} so'm")

# if-elif-else zanjirida ham else qismi majburiy emas

yosh = int(input('Yoshingiz nechida? '))
if yosh <= 4:
    price = 0
elif yosh <= 12:
    price = 5000
elif yosh < 65:
    price = 10000
elif yosh >= 65:
    price = 8000
print(f"Sizga kirish {price} so'm")

# AND, OR OPERATORLARI
# OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan
# ko'p shartlardan biri bajarilishini tekshirishda ishlatiladi.

kun = input("Bugun nima kun?>>>")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')

# AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan
# ko'p shartlarning barchasi bajarilishini tekshirishda ishlatiladi.
# AND operatori bilan yozilgan shartlarning barchasi
# bajarilgandagina TRUE qiymati qaytadi, agar shartlardan biri
# bajarilmay qolsa ham FALSE qiymati qaytadi.

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower() == 'yakshanba' and harorat >= 30:
    print("Cho'milgani ketdik!")
elif kun.lower() == 'yakshanba' and harorat < 30:
    print("Uyda dam olamiz!")

# BIR NECHTA SHARTLARNI KETMA-KET YOZISH

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
    print("Cho'milgani ketdik!")
elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
    print("Uyda dam olamiz!")

# BOOLEAN MA'LUMOTLAR TURI
# ifodalarni solishtirishda TRUE yoki FALSE qiymatlari qaytishini
# ko'rdik. Bu qiymatlar boolean (mantiqiy) qiymatlar deb ataladi

narh = 15000  # mijoz 15000 so'mga taom oldi.
choy = True  # mijoz choy ham oldi
salat = False  # mijoz salat olmadi

if choy and salat:  # agar mijoz choy ham salat ham olgan bo'lsa
    narh = narh + 10000  # narhga 10000 so'm qo'shamiz
elif choy or salat:  # agar choy yoki salat olgan bo'lsa
    narh = narh + 5000  # narhga 5000 so'm qo'shamiz

print(f"Jami {narh} so'm")  # yakuniy narhni chiqaramiz

# TODO Boolean o'zgaruvchilarni saqlashda TRUE va FALSE
#  qiymatlari o'rniga 1 va 0 sonlarini ham ishlatish mumkin.

# SHARTLARNI KETMA-KET TEKSHIRISH

narh = 15000  # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
# Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:  # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:  # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot:  # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti:  # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000

print(f"Jami {narh} so'm")

# RO'YXAT TARKIBINI TEKSHIRISH
# in OPERATORI

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunday ovqat yo\'q')

# not in OPERATORI

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')

# TODO not operatorini boshqa shartlarning oldidan ham
#  qo'yishimiz mumkin. Misol uchun: if not a==5 ifodasi
#  if a!=5 ifodasi bilan bir hil natija qaytaradi.

# IKKI RO'YXATNI SOLISHTIRISH

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")

# RO'YXAT BO'SH EMASLIGINI TEKSHIRISH

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

if buyurtmalar:  # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:  # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")
