daftarbuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print ("PROGRAM PERHITUNGAN HARGA BUAH")
print ('\n')
print ("Daftar harga buah per kilogram")
print (daftarbuah,'\n')
while (status == True):
    print('Menu :')
    print('A.Beli buah')
    print('B.Tambah daftar harga buah')
    print('C.Hapus Buah dari daftar buah')
    print('D.Selesai')
    pilih = input ('\nPilihan Anda (A,B,C,D) : ')
    print()
    total = []
    if (pilih == 'A'):
        while True :
            try:
                namabuah = input ("Silakan masukkan nama buah yang ingin anda beli : ")
                if namabuah in daftarbuah:
                    kilo = int ( input ("Berapa (Kg)             : "))
                    hargaakhir = kilo * daftarbuah[namabuah]
                    total.append(hargaakhir)
                    konfirmasi = input ("Apakah anda ingin membeli buah yang lain? (y/n) : ")
                if (konfirmasi != 'y'):
                    print("====================================")
                    print("Total harga                 : Rp", sum(total))
                    break
                elif (namabuah == '') or (namabuah not in daftarbuah):
                    print ("Maaf, buah yang ingin Anda beli tidak ada di dalam daftar")
            except (ValueError):
                    print ("Silakan masukkan jumlah (Kg) yang benar")
    elif (pilih == 'B'):
        n = True
        while ( n== True) :
                buahtambahan = input ("Silakan masukkan nama buah baru yang ingin anda jual : ")
                if buahtambahan in daftarbuah:
                    print (buahtambahan, 'buah yang anda inginkan sudah ada di dalam daftar')
                elif buahtambahan not in daftarbuah:
                    try:
                        hargatambahan = int ( input ('Harga @kg :'))
                        daftarbuah[buahtambahan] = hargatambahan
                        print(buahtambahan, 'berhasil dimasukkan\n')
                        print('Daftar Harga buah yang baru \n')
                        for data in daftarbuah:
                            print (data, '(Rp',daftarbuah.get(data),')')
                            n= False
                        print()
                    except (ValueError):
                        print('Maaf, Mohon masukkan harga yang benar')

    elif (pilih== 'C'):
        k = True
        while ( k == True):
                hapusbuah = input ('Silakan ketik nama buah yang ingin anda hapus dari daftar :')
                if hapusbuah not in daftarbuah:
                    print('bahwa',hapusbuah,'tidak ada atau habis')
                elif hapusbuah in daftarbuah:
                    del daftarbuah[hapusbuah]
                    print('buah',hapusbuah,'telah dihapus\nSilakan kembali ke menu\n')
                    print('Daftar Buah yang tersisa',daftarbuah)

                k = False
            
            
                        
    elif (pilih == 'D'):
        print('\n')
        print('Terimakasih telah menggunakan jasa pelayanan kami')
        break
