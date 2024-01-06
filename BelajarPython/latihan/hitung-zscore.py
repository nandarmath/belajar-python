from scipy import stats

zscore = float(input("Masukkan Nilai z-hitung : "))
p = stats.norm.cdf(zscore)
print("Nilai z-tabelnya adalah {}".format(p))
