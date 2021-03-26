# Input umur
umur = int(input("Berapa umur Anda?" ))

# Menampikan hasil seleksi umur >=21
if umur >= 21:

# Status ujian apabila umur >= 21
    Status_ujian = input ("Apakah Anda lulus ujian kualifikasi? [Y/T]: ")
    if Status_ujian == "Y":
        print("Anda cukup umur.")
    elif Status_ujian == "T":
        print("Anda tidak cukup umur.")

# Menampikan hasil seleksi umur <21
else:
    print("Anda tidak cukup umur.")