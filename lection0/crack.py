from string import ascii_letters, digits, punctuation # імпорт набору символів

for i in ascii_letters + digits + punctuation:          # перша позиція
    for j in ascii_letters + digits + punctuation:      # друга позиція
        for k in ascii_letters + digits + punctuation:   # третя позиція
            for l in ascii_letters + digits + punctuation: # четверта позиція
                print(i, j, k, l) # вивести комбінацію з пробілами між цифрами

