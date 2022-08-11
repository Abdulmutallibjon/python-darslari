print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting:\n")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

# 3

sevimli_serial = {}
sevimli_kino = []
ishora = True
while ishora:
    ism = input("Ismingiz nima?\n")
    # for q in ishora:
    kino = list(input(f"Salom {ism.title()}.\n"
                      f"Sevimli kino va serialingiz nomini yozing,\n"
                      f"agar yo`q bo`lsa 'yo`q' deb yozing,\n"
                      f"ro`yhatingiz tugasa 'tugadi' deb yozing:\n"))
    sevimli_serial['ism'] = ism
    # sevimli_kino.append(kino)
    sevimli_serial['kino'] = kino

    # javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    # if javob == "yo'q":
    #     ishora = False

    if kino and ism == "tugadi":
        ishora = False
    elif kino and ism == "yo`q":
        print("Javobingiz uchun rahmat!")
        ishora = False
for a in sevimli_serial.items():
    print(f"{sevimli_serial['ism']}ning sevimli kinolari:\n")
    for b in a['kino']:
        print(b)

#
#
# if kino.lower() == "tugadi":
#     for a in sevimli_serial:
#        print(f"{sevim li_serial['ism']}ning sevimli kinolari:\n")
#         for b in sevimli_serial['kino']:
#             print(b)
# elif kino.lower() == "yo`q":
#     print(f"Javobingiz uchun rahmat!\n"
#           f"\n{ism}")
# # ismlar = []
# # ismlar.append(ism)
# # for i in ismlar:
# #     if len(ismlar) == 2:
# #         break
