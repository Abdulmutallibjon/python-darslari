# LIST (RO'YXAT)
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]    # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000]  # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5]   # sonlar va matnlar aralash ro'yxat
# ismlar = []   # bo'sh ro'yxat

# LIST ELEMENTLARI
mevalar1 = ['olma', 'anjir', 'shaftoli', "o'rik"]  # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar1[0])
print("Ikkinchi meva: ", mevalar1[1])

# Agar list ichidagi elementlar matn ko'rinishid bo'lsa,
# ularga string metodlarni qo'llashimiz mumkin:
print("Birinchi meva: ", mevalar1[0].title())
print("Ikkinchi meva: ", mevalar1[1].upper())

# List elementlari ustida arifmetik amallar bajarish:
narhlari = [12000, 18000, 10900, 22000]
print(narhlari[2] + narhlari[3])

# Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin.
# Bu usul Listning uzunligini bilmaganda juda asqotadi.
car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1])   # Listning eng oxirgi elementiga -1 bilan murojat qilamiz

# ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
#  Elementni o'zgartirish
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000  # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000  # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000  # 4-qiymatga 2000 qo'shamiz
print(narhlar)

# Yangi element qo'shish
# .append() metodi yordamida ro'yxatning oxiriga qiymat qo'shish:
fruits = ['behi', 'nok', 'olcha', "banan"]
fruits.append("tarvuz")  # mevalar ga tarvuz qo'shamiz
print(fruits)

# .append() metodi bo'sh ro'yxatni to'ldrisihda juda qulay usul.
# Odatda dastur boshida bo'sh ro'yxat yaratilib, dastur davomida ro'yxat
# foydalanuvchi tomonidan to'ldirib borilishi odatiy hol.
cars = []   # bo'sh ro'yxat yaratamiz
cars.append('Lacetti')  # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3')  # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
print(cars)

#  .insert() metodi - Ro'yxatning istalgan joyiga yangi element qo'shish uchun
#  bu metoddan foydalanamiz. .insert() metodi ichida yangi elementning
#  indeksi va qiymati beriladi
cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu')  # 1-o'ringa yangi qiymat qo'shamiz
print(cars)

cars.insert(2, 'Damas')  # 3-o'ringa yangi qiymat qo'shamiz
print(cars)

# Elementni o'chirish
# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki
# qiymatini bilishimiz lozim.
# Indeks yordamida olib tashlash uchun -> del <- operatoridan foydalanamiz
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1]  # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)

# .remove(qiymat) metodidan - Element qiymati bo'yichi o'chirish uchun \
# foydalanamiz. Buning uchun qavs ichida o'chirib tashlash kerak
# bo'lgan qiymatni yozamiz
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli')  # Ro'yxatdan shaftolini o'chirdik
print(mevalar)

# .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi
# qiymatni o'chiradi. Agar ro'yxatning ichida 2 va undan ko'p bir hil
# qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk")  # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
print(hayvonlar)

# Elementni sug'urib olish
# .pop(indeks) - Ba'zida biror elementni butunlay o'chirib tashlash emas,
# balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi
# mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)  # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)

# Agar .pop() metodida indeks berilmasa,
# ro'yxatdan o'xirgi qiymat sug'urib olinadi.
bozorlik1 = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot1 = bozorlik1.pop()  # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot1 + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik1)