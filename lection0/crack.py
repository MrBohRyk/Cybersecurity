from string import digits # імпорт набору цифр '0123456789'
for i in digits:          # перша позиція
    for j in digits:      # друга позиція
        for k in digits:   # третя позиція
            for l in digits:  # четверта позиція
                print(i, j, k, l) # вивести комбінацію з пробілами між цифрами