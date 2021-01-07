import sys

listTemp = []
jumlah = 0
transaksi = []
nama = input("Halo user silahkan input nama anda :")
bulan = input("inputkan bulan pembukuan :")
x = len(listTemp)
arr = 0

while True:
    print('tekan (1) untuk input data, (2) untuk print data input, (q) keluar program')
    userinput = input()
    if userinput == 'q':
        sys.exit()
    if userinput == '2':
        print("===========================================|")
        print("       Laporan "+nama+" dibulan "+bulan+"          |")
        print("===========================================|")
        print("Tanggal | Nama Transaksi  |     Jumlah     |")
        print("-------------------------------------------|")
        for r in listTemp:
            for c in r:
                print(c, end="       |      ")
            print()
        for tanggal, namaTransaksi, jumlahTransaksi in listTemp:
            jumlah += jumlahTransaksi
        print("-------------------------------------------|")
        print("Total:                          " + str(jumlah)+"      |")
        print("-------------------------------------------|")
    if userinput == '1':
        tanggal = int(input("Input tanggal transaksi : "))
        namaTransaksi = input("Input Jenis transaksi : ")
        jumlahTransaksi = int(input("Input Jumlah transaksi : "))
        transaksi.append(tanggal)
        transaksi.append(namaTransaksi)
        transaksi.append(jumlahTransaksi)
        listTemp.insert(arr+1, transaksi)
        transaksi = []
        print("Data Tersimpan")
