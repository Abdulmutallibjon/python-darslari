# 18-dars: WHILE VA RO'YXATLAR

savat = []
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != "ha":
        break
print("Dastur tugadi!")