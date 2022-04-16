
def length(arrayName): #len(arr)
    panjang = 0
    for row in arrayName:
        panjang += 1
    return (panjang)

def saldovalid (saldo, balance) :
    if balance + saldo > 0 : return True
    else : return False

def plus_arr (arr1,arr2): #arr.append
    return arr1+arr2

def remove_last (arr): #arr.pop
    arr_baru = [0 for i in range (length(arr))]
    for i in range (length(arr)-1):
        arr_baru[i] = arr[i]
    return arr_baru

def 
