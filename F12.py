from array_csv import user
from perpustakaan_fungsi import length, saldovalid

def topup (user) :
    username = "Masukan username: "
    saldo = "Masukan saldo: "
    isunamevalid = False

    for i in range(1, length(user)) : 
            if username == user[i][1] :
                isunamevalid = True
                nama = user[i][2]
                balance = int(user[i][5])
                break

    if isunamevalid :
        if saldovalid(saldo, balance) : 
            newbalance = balance + saldo
            user[i][5] = str(newbalance)
            print("Top up berhasil. Saldo {nama} bertambah menjadi {newbalance}.")
        else : print("Masukan tidak valid")
    return user







