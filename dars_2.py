# STRING (matn) - Pythondagi eng mashxur ma'lumot turlaridan biri.
# Avvalgi darsda ko'rganimizdek, o'zgaruvchiga matn yuklash uchun
# matn qo'shtirnoq (" ") yoki birtirnoq (' ') ichida yozilishi kerak.

# Pythonda matnlar Unicode jadvalidagi istalgan belgilaridan
# iborat bo'lishi mumkin (jumladan o'zbek, arab, hind, xitoy alifbosidagi
# harflar yoki turli emoji-smayliklar).

# Unicode jadvalini < unicode-table.com > dan olishimiz mumkin
matn = "Men yangi 📱 oldim"
print(matn)


# STRING USTIDA AMALLAR

# Matnlarni qo'shish operatori (+)
ism = 'Ahmad'
print("Mening ismim " + ism)

ism = 'Ahad '       # matn ohirida bo`sh joy tashlang, konsolga chiqqanda
familiya = 'Qayum'  # keyingi so`zga qo`shilib qolmasligi uchun
print(ism + familiya)

# yoki matn ajratish uchun shunday qilsak ham bo`ladi
ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya)  # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

# f-string - Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni
# birlashtirish uchun f-string usulidan
# f"{matn1} {matn2}" ham foydalansak bo'ladi:
ism = "James"
familiya = 'Bond'
print(f"Salom, men {familiya}. {ism} {familiya}man!")

# Mahsus belgilar - Matnga bo'shliq qo'shish uchun \t belgisidan,
# yangi qatordan boshlash uchun \n belgisidan foydalanamiz:
print('Hello world! 1')
print('Hello \tworld! 2')
print('Hello \nworld! 3')

# STRING METODLARI
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.
print(ism_sharif.upper())
# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
print(ism_sharif.lower())
# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
print(ism_sharif.title())
# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
print(ism_sharif.capitalize())

# Metodlarni faqat o'zgaruvchilarga emas,
# balki to'g'ridan-to'g'ri matnga ham qo'llash mumkin
# (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning) manzili xolos)
print('james bond'.upper())

# strip(), rstrip() va lstrip() metodlari
meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
# lstrip() — matn boshidagi bo'shliqni
print("Men " + meva.rstrip() + " yaxshi ko'raman")
# rstrip() – matn oxiridagi bo'shliqni
print("Men " + meva.strip() + " yaxshi ko'raman")
# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
print("Men " + meva + " yaxshi ko'raman")

# INPUT — FOYDALANUVCHI BILAN MULOQOT
# ism = input("Ismingiz nima?")
# print("Assalomu alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>")  # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalomu alaykum, " + ism.title())
