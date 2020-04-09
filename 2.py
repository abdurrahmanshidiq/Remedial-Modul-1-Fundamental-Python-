tahun = int(input('User Input : '))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            res = 'Tahun Kabisat'
        else:
            res = 'Bukan Tahun Kabisat'
    else:
        res = 'Tahun Kabisat'
else:
    res = 'Bukan Tahun Kabisat'


print(f'Output : {res}')