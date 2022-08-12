# To'plam yaratish
sonlar = {1, 2, 3}
ismlar = {"alijon", "valijon", "boqijon"}
mevalar = set()
sonlar = {1, 2, 3, 3, 4, 4, 5, 6}
print(sonlar)

# Ro'yxatdan to'plamga o'tish
mevalar = ["olma", "anjir", "olma", "uzum", "olma", "uzum"]
mevalar = set(mevalar)
print(mevalar)

# To'plamga element qo'shish
mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
mevalar.add("banan")
print(mevalar)
mevalar.update(["anor", "qovun"])
print(mevalar)

# Element o'chirish
mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
mevalar.discard("anjir")
print(mevalar)
mevalar.remove("banan")
print(mevalar)

sonlar = {0, 1, 2, 3, 4, 5, 6, 7}
sonlar.discard(7)
print(sonlar)
sonlar.remove(5)
print(sonlar)

sonlar = {1, 2, 3, 4, 5, 6}
son = sonlar.pop()
print(son)
print(sonlar)

# To'plamlar ustida amallar

# Jamlanma
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = A | B
print(C)
D = A.union(B)
print(D)

# Kesishma
print(A & B)
print(A.intersection(B))

# Farq
print(A - B)
print(B.difference(A))

# Simmetrik farq
print(A ^ B)
print(A.symmetric_difference(B))
