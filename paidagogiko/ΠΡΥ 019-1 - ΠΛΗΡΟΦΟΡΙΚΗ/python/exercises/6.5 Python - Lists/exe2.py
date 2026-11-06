# Άσκηση 2: insert, pop(2), append
# ["Thanasis"] -> ["Thanasis", "Anna"] -> ["Swtiris", "Thanasis", "Anna"]
# το pop(2) αφαιρεί την "Anna" -> ["Swtiris", "Thanasis", "Marios"]

onomata = ["Thanasis"]
onomata.insert(1, "Anna")
onomata.insert(0, "Swtiris")
onomata.pop(2)
onomata.append("Marios")
print(onomata)
