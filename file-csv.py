import csv

siswa = [
    ("Adi", "A", 90),
    ("Budi", "A", 80),
    ("Yuni", "B", 76),
    ("Reny", "C", 85),
    ("Evi", "B", 76),
]

# buat file csv
f = open("data.csv", "w")
tulis = csv.writer(f)

# menulis dan memberikan label kolom

tulis.writerow(("Nama", "Kelas", "Nilai"))

# menulis file csv

for i in siswa:
    tulis.writerow(i)

f.close()
