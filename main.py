import sys
from prettytable import PrettyTable


sum = 0

x = PrettyTable()
x.field_names = ["Tanggal", "Nama Transaksi", "Jumlah"]
x.align["Jumlah"]= "r"
x.add_rows(
    [
        [1, "asdasdasdas" , "cacaca"],
        [2, "aasasdasdqwe" , "gagaga"],
    ]
)


def header():
    print("=================================================")
    print("Laporan Transaksi Pembukuan si Budi bulan Januari")
    print("=================================================")

def footer():


    print("-------------------------------------")
    print("Total                              "+str(sum)+"|")
    print("-------------------------------------")


header()
print(x)
footer()
