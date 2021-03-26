# Input beban bagasi maksimal
bebanmaks_lbs = 50
bebanmaks_kg = bebanmaks_lbs * 0.453592
beban110 = 110
beban49 = 49

# Seleksi pertama = 110 kg
seleksipertama = bebanmaks_kg > beban110
print(seleksipertama)

# Seleksi kedua = 49 kg
seleksikedua = bebanmaks_kg > beban49
print(seleksikedua)