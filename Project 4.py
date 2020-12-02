#Latihan Nomor 4
daftarSayuran = ['bayam', 'kangkung', 'wortel', 'selada']
print ('PROGRAM BELANJA SAYURAN')
print ("Sayuran yang ada saat ini : ", daftarSayuran)
print ("\nBerikut menunya, silakan dipilih\n")
while True :
    print ('Menu yang ada :\n') 
    print ('A. Tambahkan sayuran lain')
    print ('B. Hapus data sayuran')
    print ('C. Tampilkan daftar sayuran')
    print ('D. Selesai :)\n')
    pilih = input ("Pilihan Anda (A,B,C,D) : ")
    if (pilih == 'A'):
        tambahSayuran = str ( input ("Nama sayuran yang ingin ditambahkan : "))
        print (tambahSayuran, "sudah dimasukkan dalam daftar\n")
        daftarSayuran.append (tambahSayuran)
    elif (pilih == 'B'):
        i = True
        while (i == True):
            try:
                hapussayuran = str ( input ("Nama sayuran yang ingin dihapus : "))
                daftarSayuran.remove(hapus)
                print(hapussayuran, "telah dihapus dari daftar \n")
                i = False
            except (ValueError):
                print ("Maaf, sayuran tidak ditemukan dalam daftar")
    
    elif (pilih == 'C') :
        print("isi daftar sekarang : ", daftarSayuran, "\n")
    elif (pilih == 'D'):
        keluar = input ("Apakah Belanja anda sudah selesai ? (y/n) : ")
        if keluar == 'y':
            break
