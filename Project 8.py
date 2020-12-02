daftarbuah = { 'Apel'  : 5000,'Jeruk' : 8500,'Mangga': 7800,'Duku'  : 6500 }

def Average (daftarbuah):
    harga = 0
    sum = 0

    for r,y in daftarbuah.items():
        harga += y
        sum += 1

    rerata = harga/sum
    return rerata
    
def Average1(daftarbuah):
    harga1 = list(fruit.values())
    rerata1 = sum(harga1)/len(harga1)
    return rerata2



hasilakhir = Average(daftarbuah)
print('Rata-rata harga satuan buah adalah ',hasilakhir)

