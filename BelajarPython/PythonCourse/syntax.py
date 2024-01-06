print(
    "hi\
how are you?"
)

# Multi line comment
print(
    """Belajar
 b = 10
 Bahasa Python"""
)


if 2 > 1:
    print("2 is greter")

x = 5
y = "printer"
print(" i bu %s a %s at shop" % (x, y))
print("i buy {} a {} at shop".format(x, y))

print(f"i buy {x} a {y} at shop")
a = 10
print(a)


def tambah(x, y):
    """INi fungsi penjumlahan"""
    b = x + y
    print("hasil dari {} + {} adalah = {}".format(x, y, b))


tambah(5, 8)
print(tambah.__doc__)
