# Nama  : Bagus Mulyo Firmansyah
# Nim   : 04319053
# Prodi : Teknik Informatika / Bagus

#untuk membuat validasi benar integer atau salah
def inputAngka(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Bukan Angka !")
            continue
        else:
            return userInput
            break
#program utama yang ditampilkan
angka = inputAngka("Masukan Angka : ")

if type(angka) is int:
    print("Validasi : Ya benar itu angka/integer")