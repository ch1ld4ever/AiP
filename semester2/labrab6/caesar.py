al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
choice = int(input())

if choice == 1:   # 1 - зашифровать
    val = input()
    key = int(input())
    val_low = val.lower()
    vald = ""

    for letter in val_low:
        position = al.find(letter)
        new_position = position + key 
        if letter in al:
            vald = vald + al[new_position]
        else: 
            vald = vald + letter 
    print(vald)

elif choice == 2:  # 2 - расшифровать
    val = input()
    key = int(input())  
    val_low = val.lower()
    vald = ""

    for letter in val_low:
        position = al.find(letter)
        new_position = position - key 
        if letter in al:
            vald = vald + al[new_position]
        else: 
            vald = vald + letter 
    print(vald)
      