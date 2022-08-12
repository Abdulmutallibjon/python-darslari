# 16 NESTING
# Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki
# boshqa lug'atni, yoki aksincha ro'yxat ichida lug'atni saqlash ham
# qo'l kelishi mumkin. Bu ingliz tilida Nesting deyiladi.
# Nesting Pythondagi foydali xususiyatlardan biri.

# LUG'ATLAR RO'YXATI

car0 = {
    'model': 'lacetti',
    'rang': 'oq',
    'yil': 2018,
    'narh': 13000,
    'km': 50000,
    'korobka': 'avtomat'
}

car1 = {
    'model': 'nexia 3',
    'rang': 'qora',
    'yil': 2015,
    'narh': 9000,
    'km': 89000,
    'korobka': 'mexanika'
}

car2 = {
    'model': 'gentra',
    'rang': 'qizil',
    'yil': 2019,
    'narh': 15000,
    'km': 20000,
    'korobka': 'mexanika'
}

# Agar biz har bir lug'atga alohida murojat qiladigan bo'lsak,
# lug'atlarning nomlarini yodlab qolishimiz talab qilinar edi

car = car0
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car1
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car2
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

# Keling, barcha avtolarni bitta ro'yxatga joylaymiz,
# va for tsikli yordamida birma-bir konsolga chiqaramiz
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")

# for tsikli yordamida biz bo'sh lug'atlar
# ro'yxatini ham yaratib olishimiz mumkin:

malibus = []  # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = {  # har bir yangi mashina uchun lug'at yaratamiz
        'model': 'malibu',
        'rang': None,  # rangi noaniq
        'yil': 2020,
        'narh': None,  # narhi belgilanmagan
        'km': 0,
        'korobka': 'avto'
    }
    malibus.append(new_car)  # yangi lug'atni ro'yxatga qo'shamiz

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

for malibu in malibus[6:]:  # ohirgi 4 ta mashinani
    malibu['rang'] = 'qora'  # rangi qora
    malibu['korobka'] = 'mexanika'  # korobkasi mexanika

for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000
print(malibus)

# LUG'AT ICHIDA RO'YXAT

dasturchilar = {
    'ali': ['python', 'c++'],
    'vali': ['html', 'css', 'js'],
    'hasan': ['php', 'sql'],
    'husan': ['python', 'php'],
    'maryam': ['c++', 'c#']
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')

# LUG'AT ICHIDA LUG'AT

hamkasblar = {
    'ali': {'familiya': 'valiyev',
            'tyil': 1995,
            'malumot': 'oliy',
            'tillar': ['python', 'c++']
            },
    'vali': {'familiya': 'aliyev',
             'tyil': 2001,
             'malumot': "o'rta-maxsus",
             'tillar': ['html', 'css', 'js']},
    'hasan': {'familiya': 'husanov',
              'tyil': 1999,
              'malumot': 'maxsus',
              'tillar': ['python', 'php']}
}

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())

# AMALIYOT

# 1

mashxur_shaxslar1 = {
    'adi': 'Abu Abdulloh Muhammad ibn Ismoil',
    'dyil': '810',
    'dyeri': 'Buxoro',
    'yasi': '60'
}
mashxur_shaxslar2 = {
    'adi': 'Abdulla Qodiriy',
    'dyil': '1894',
    'dyeri': 'Toshkent',
    'yasi': '44'
}
mashxur_shaxslar3 = {
    'adi': 'Erkin Vohidov',
    'dyil': '1936',
    'dyeri': 'Farg`ona',
    'yasi': '80'
}
mashxur_shaxslar4 = {
    'adi': 'Alisher Navoiy',
    'dyil': '1441',
    'dyeri': 'Xirot',
    'yasi': '60'
}
mashxur_shaxslar = [mashxur_shaxslar1, mashxur_shaxslar2, mashxur_shaxslar3, mashxur_shaxslar4]

for mashxur in mashxur_shaxslar:
    print(
        f"{mashxur['adi'].title()} {mashxur['dyil']}-yilda {mashxur['dyeri']}da tavallud topgan. {mashxur['yasi']} yil umr ko`rgan.")

# 2

mashxur_shaxslar1['asarlari'] = ["Al-jome` as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix al-sag`ir"]
mashxur_shaxslar2['asarlari'] = ["O`tgan kunlar", "Mehrobdan chayon", "Obid ketmon"]
mashxur_shaxslar3['asarlari'] = ["Tong nafasi", "Qo`shiqlarim sizga", "O`zbegim", "Qiziquvchan Matmusa"]
mashxur_shaxslar4['asarlari'] = ["Hamsa", "Lison ut-Tayr", "Mahbub ul-Qulub", "Munojot"]

for mashxur in mashxur_shaxslar:
    print(f"\n{mashxur['adi'].title()}ning mashxur asarlari: ")
    for asar in mashxur['asarlari']:
        print(asar)

# 3

oila_azolari = {
    'ali': ['Terminator', 'Rembo', 'Titanic'],
    'vali': ['Tenet', 'Inception', 'Interstellar'],
    'gani': ['Abdullajon', 'Bomba', 'Shaytanat']
}

for azo, kinosi in oila_azolari.items():
    print(f"\n{azo.title()}ning sevimli kinolari:")
    for kino in kinosi:
        print(kino)

# 4

davlatlar = {
    "O`zbekiston": {
        'Poytaxti': 'Toshkent',
        'Hududi': '448978 kv.km',
        'Aholisi': '38000000',
        'Pul birligi': "so`m"
    },
    "Rossiya": {
        'Poytaxti': 'Moskva',
        'Hududi': '17098246 kv.km',
        'Aholisi': '144000000',
        'Pul birligi': 'rubl'
    },
    'AQSH': {
        'Poytaxti': 'Vashington',
        'Hududi': '9631418 kv.km',
        'Aholisi': '327000000',
        'Pul birligi': "dollar"
    },
    'Malayziya': {
        'Poytaxti': 'Kuala-Lumpur',
        'Hududi': '329750 kv.km',
        'Aholisi': '25000000',
        'Pul birligi': "rinngit"
    }
}

for davlat, malumoti in davlatlar.items():
    print(f"{davlat}ning poytaxti {malumoti['Poytaxti']}"
          f"{malumoti[0:4]}: {malumoti['Hududi']}")
