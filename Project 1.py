#Latihan Nomor 1
try :
    listAngka = []
    i = 0
    banyakBil = int ( input ("Silakan masukkan banyak bilangan yang anda inginkan : "))
    while(i < banyakBil):
        angka = int ( input ("Silakan masukkan angka pilihanmu : "))
        listAngka.append(angka)
        i+=1

    listAngka.sort(reverse = True)
    print ("Urutan bilangan dari besar ke kecil yang berasal dari angka yang telah anda masukkan adalah\n",listAngka)
except (ValueError):
    print ("Mohon maaf, silakan masukkan angka yang memenuhi :)")
