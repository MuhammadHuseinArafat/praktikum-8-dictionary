#Latihan Nomor 3
print ("Selamat datang di Program Input Nama Mahasiswa")
print ('----------------------------------------------')
print ('Silakan ikuti Langkah-langkah di bawah yaa\n')       
try:
    
    status = True
    n = []
    while (status == True):
        namaMhs = str ( input ("Silakan masukkan nama mahasiswa/i : "))
        n.append(namaMhs)
        konfirmasi = input ("Apakah kamu ingin menambah nama mahasiswa lagi? (ya/tidak) : ")
        n.sort()
        if (konfirmasi != 'ya'):
            print()
            for data in n:
                print (data, "(", len(data), "karakter", ")")
                status = False 
except ValueError:
    print("Mohon masukkan data dengan Benar")
