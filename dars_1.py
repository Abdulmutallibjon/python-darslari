# print - funksiyasi matnni konsolga chiqarish kodi
print("Hello world 1")

# kod yozishda biron belgi yozilmasa yoki kam bo`lsa dastur ishlashida
# < Syntax Error > ya`ni sinteks hatolik beradi

# bir yoki qo`sh tirnoqdan foydalanish kerak print funksiyasida
# matnni konsolga chiqarish uchun
print('Hello world 2')
print("Hello world 3")

# """ ff """ yoki < bek slesh n > yani < \n > yordamida
# matnni qatorga bo`lishimiz mumkin
print("""Hello 
world 4""")                 # 3 talik qo`sh tirnoq
print("Hello \nworld 5")    # qo`sh tirnoq
print('Hello \nworld 6')    # bir tirnoq

# matn ichida bir yoki ikki tirnoqni konsolga chiqarish uchun < bek slesh >
# yani < \ > dan foydalanamiz
print("Men \"Acer\" dan foydalanaman")

# yoki matn ichida bir tashqarida qo`sh, yoki teskarisi matnni bir
# ichida esa qo`sh tirnoqdan foydalanish kerak
print('Men "Apple" dan foydalanaman')
print("Men 'Iphone' dan foydalanaman")

# qatorni nushasini pastki qatorga ko'chirish uchun < ctrl + d > foydalanamiz

# kodni izohga yoki konsolga chiqarishda programma o`qimasligi uchun
# < ctrl + slesh "\" > bosamiz english klavishda

# Arifmetik amallar bajarish
# Qo`shish belgisi +
print(5+5)
# Ayrish belgisi -
print(10-2)
# Ko`paytirish belgisi *
print(5*5)
# Sonni kvadrati **
print(3**2)
# Bo`lish belgisi \ va \\ ,
# farqi \ < bir slesh > natijani o`nlik sanoq sistemasida ko`rsatadi
print(10/2)
print(11/2)
# \\  < ikki slesh > natijani butun son qilib ko`rsatadi, qoldiqni ko`rsatmaydi
print(10//2)
print(11//2)
# arifmetik amalni konsolga matn bilan chiqarish
print("3x3=", 3*3)
print('5 ning kvadrati', 5**2, "ga teng")
print("4 ning kvadrati " + str(4**2) + " ga teng")
# qoldiq ciqarish
print(11 % 2)   # % < foiz > belgisi natijani qoldig`ini ko`rsatadi
print(12 % 3)

# Qavs ichidagi amallar qavs ortidagilardan avval bajariladi
print(5+(2*2))
# Darajaga oshirish (ildiz chiqarish) ko'paytirish va bo'lishdan avval bajariladi
print(4**2//8)
# Ko'paytirish va bo'lish, qo'shish va ayirishdan avval bajariladi
print(4*4+5)
# Boshqa holatlarda ifodalar chapdan o'ngga qarab bajariladi
print()
