from string import ascii_letters # імпорт набору цифр '0123456789'
for i in ascii_letters:          # перша позиція
    for j in ascii_letters:      # друга позиція
        for k in ascii_letters:   # третя позиція
            for l in ascii_letters:  # четверта позиція
                print(i, j, k, l) # вивести комбінацію з пробілами між цифрами