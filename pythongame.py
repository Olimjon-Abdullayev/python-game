import random as r

print("############################################################################")
print("########################  SO'Z TOPISH O'YINI  #############################")
print("############################################################################\n")


def users_turn(x=10):
    print("Keling o'yin oynaymiz, men 1dan 10gacha son oyladim 🎲 siz topishingiz kerak\n")
    comp_num =  r.randint(1, x)
    tries = 0
    while True:
        tries += 1
        user_num = int(input("Tahminingizni kiriting : "))
        if user_num > comp_num:
                print("\nXato, men o'ylagan son bundan kichik, yana qayta urinib ko'ring.\n")
        elif user_num < comp_num:
                    print("\nXato, men o'ylagan son bundan katta, yana qayta urinib ko'ring.\n")
        else:
             break
    print(f"\nSiz men o'lagan sonni {tries}inchi urinishda tobdingiz, tabriklayman👏!")
    return tries


def computers_turn(x=10):
    print("\n############################################################################\n")
    input(f"\n1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    low = 1
    high = x
    tries = 0
    while True:
        tries += 1
        if low != high:
            user_number = r.randint(low,high)
        else:
            user_number = low
        responce = input(f"\nSiz {user_number} sonini o'yladingiz: To'g'ri bo'lsa (t),\n"
                      f"Agar siz o'ylagan son  bundan kattaroq bo'lsa (+),\n yoki kichikroq bo'lsa (-) >>> ".lower())
        if responce == "-":
            high = user_number - 1
        elif responce == "+":
            low = user_number + 1
        else:
            break
    print(f"\nMen {tries}inchi urinishda topdim🥳")
    return tries


def play(x=10):
    replay = True
    while replay:
        user_turn = users_turn(x)
        computer_turn = computers_turn(x)
        
        if user_turn > computer_turn:
            print(f"\nMen yutdim😉 chunki men sizdan kam {computer_turn} ta urinishda topdim.")
        elif user_turn < computer_turn:
            print(f"\nSiz yutdingiz 🏆, sonni {user_turn} ta urinishda topdingiz. ")
        else:
            print(f"\nDurrang 🤝, ikkimiz ham {computer_turn} ta urinishda topdik")
        replay = int(input("Yana o'ynaysizmi(1.Ha / 0.Yo'Q) : "))
        

play()