file_selamat = open("selamat.txt", "r")

selamat = file_selamat.readlines()

for kata in selamat:
    print(kata)

file_selamat.close()
