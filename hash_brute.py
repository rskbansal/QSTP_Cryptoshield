import hashlib

original = '5995fab51cae396a07d112e65b8337e2'

def crack():
    for i in range(10000000):
        i = str(i).zfill(7)
        if hashlib.md5(i.encode()).hexdigest() == original:
            print('Password is: ' + i)
            break

crack()