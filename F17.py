#>>> exit

import F16
import sys 

pilihan=str(input("Apakah Anda mau melakukan penyimpanan file yang telah diubah? (y/n) "))

while not ((pilihan=='Y') or (pilihan=='y') or (pilihan=='N') or (pilihan=='n')):
    pilihan=str(input("Apakah Anda mau melakukan penyimpanan file yang telah diubah? (y/n) "))

if (pilihan=='Y') or (pilihan=='y'):
    F16.save()

else:
    sys.exit()
