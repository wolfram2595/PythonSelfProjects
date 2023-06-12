import time
import random

print("Bun venit din partea creatorului meu Bejenaru Sebastian!\nPoftim o moneda de 50 de bani, dai cu banul!")
choice = input("Cap sau pajura?\n").lower()
time.sleep(1)
print("Ai dat cu banul!")
time.sleep(1)
random_int = random.randint(0, 1)
if random_int == 1:
    print("A rezultat Cap!")
    time.sleep(1)
    if choice == "cap":
        print(f"Pentru ca ai ales {choice}, ai castigat!")
    else:
        print(f"Pentru ca ai ales {choice}, ai pierdut!")
else:
    print("A rezultat Pajura!")
    time.sleep(1)
    if choice == "pajura":
        print(f"Pentru ca ai ales {choice}, ai castigat!")
    else:
        print(f"Pentru ca ai ales {choice}, ai pierdut!")