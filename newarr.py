import sys
from prettytable import PrettyTable 

t = PrettyTable()
listTemp = []
t.field_names = ["Tanggal", "Nama Transaksi", "Jumlah Transaksi"]
t.add_row([0, "Indomaret", 30000])
t.add_row([1, "Alfamart", 4999])
jumlah = 0
transaksi = []
nama = input("Halo user silahkan input nama anda :")
bulan = input("inputkan bulan pembukuan :")

def insert():
    x = len(listTemp)
    listTemp.insert(x+1, transaksi)
    tanggal = int(input())
    namaTransaksi = str(input())
    jumlahTransaksi = int(input())

while True:
    print('tekan (1) untuk input data, (2) untuk print data input, (q) keluar program')
    userinput = input()
    if userinput == 'q':
        sys.exit()
    if userinput == '2':
        print("==================================")
        print("  Laporan "+nama+" dibulan "+bulan+"  ")
        print("==================================")
        print(t)
        print("Total ===========")
        break
    if userinput == '1':
        x = len(listTemp)
        print(x)
        listTemp.insert(x+1, transaksi)
        tanggal = int(input("tanggal transaksi"))
        namaTransaksi = input("Jenis transaksi : ")
        jumlahTransaksi = int(input("Jumlah transaksi : "))

        transaksi.append(tanggal)
        transaksi.append(namaTransaksi)
        transaksi.append(jumlahTransaksi)
        listTemp.append(transaksi)
        print(listTemp)
