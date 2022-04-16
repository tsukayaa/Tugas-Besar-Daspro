from perpustakaan_fungsi import length

def topup () :
    global user_data
    username = input("Masukan username: ")
    saldo = input("Masukan saldo: ")
    isunamevalid = False

    for i in range(0, length(user_data)) :
            if username == user_data[i][1] :
                isunamevalid = True
                nama = user_data[i][2]
                balance = int(user_data[i][5])
                urutanID = i
    
    if(not isunamevalid):
        print(f"Username {username} tidak ditemukan.")
    else:
        if (int(user_data[urutanID][5]) + int(saldo)) < 0 :
            print("Masukan tidak valid.")
        else :
            newbalance = int(saldo) + balance
            user_data[urutanID][5] = str(newbalance)
            print(f"Top up berhasil. Saldo {nama} bertambah menjadi {newbalance}.")
    return user
topup()







