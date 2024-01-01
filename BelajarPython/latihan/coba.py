print("yang berjalan adalah ={}".format(__name__))

print("sebelum import numpy")
import numpy as np

print("sebelum menjalankan fungsi numpy")


def fungsi_np():
    print("hasil kali array* 2={}".format(np.array([12, 3]) * 2))


print("sebelum menjalanakan __name__=='__main__'")
if __name__ == "__main__":
    fungsi_np()
    print("coba.py sedang dijalankan langsung")
else:
    print("coba.py sedang diimpor")

print("Setelah menjalankan __name__=='__main__'")
