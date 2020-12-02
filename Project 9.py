#Latihan Nomor 9

daftarbuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print ("PROGRAM PERHITUNGAN HARGA BUAH")
print ('\n')
print ("Daftar harga buah per kilogram")
print (daftarbuah,'\n')
while True:
    namabuah = input ("Silakan masukkan nama buah yang ingin anda beli : ")
    if namabuah in daftarbuah:
        try:
            kilo = int ( input ("Berapa (Kg)            : "))
            harga = kilo * daftarbuah[namabuah]
            print("-------------------------------")
            print("Total harga                 : Rp", harga)
            break
        except (ValueError):
            print ("Silakan masukkan jumlah (Kg) yang benar")
            break
    elif (namabuah == '') or (namabuah not in daftarbuah):
        print ("Maaf, buah yang ingin Anda beli tidak ada di dalam daftar")
