
def length(arrayName):
    panjang = 0
    for row in arrayName:
        panjang += 1
    return (panjang)

def saldovalid (saldo, balance) :
    if balance + saldo > 0 : return True
    else : return False
