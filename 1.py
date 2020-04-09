list_word = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']

inWord = input('Masukkan Kata : ')


def filterWord(lisTxt):
    for i in list_word:
        if inWord.lower() in lisTxt.lower():
            return True
        else:
            return False
filtered = filter(filterWord, list_word)

finalRes=[]
for i in filtered:
    finalRes.append(i)

print(f'Output : {finalRes}')




