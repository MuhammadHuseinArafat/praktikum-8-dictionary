#latian nomor 7
daftarbuah = { 'Apel'  : 5000,'Jeruk' : 8500,'Mangga': 7800,'Duku'  : 6500 }

def palingMahal (a):
    nilaiMax = max(a, key=a.get)
    print(nilaiMax)


print('Harga buah yang satuannya paling mahal adalah :')
palingMahal(daftarbuah)
