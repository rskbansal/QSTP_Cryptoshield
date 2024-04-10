import hashlib

pref = 'qstp-'
suff = '-is-fun'

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        s = pref + str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + suff
                        h = hashlib.md5(s.encode()).hexdigest()
                        if h == 'adc351dc969292b15daa4fe0e036c5f9':
                            print(s)
                            exit(0)