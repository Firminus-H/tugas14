# Nama  : Firminus Honoratus
# Nim   : 04319001
# Prodi : Teknik Informatika / B

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
    print("Validasi : Ya benar itu angka/int")