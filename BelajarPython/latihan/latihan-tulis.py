print("Progres Menulis file teks                  ")
print("############################################")

# ambil input dari user

nama = input("Nama :")
umur = input("Umur  :")
alamat = input("Alamat : ")

# format text
teks = "Nama : {}\nAlamat   : {}\nUmur  : {}\n ----------------------------------------\n".format(
    nama, alamat, umur
)
# buka file untuk dituliks
#
file_tulis = open("biodata.txt", "a")

file_tulis.write(teks)

file_tulis.close()
