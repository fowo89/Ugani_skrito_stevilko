# -*- coding: utf-8 -*-

import random

def main():

    secret = random.randint(1,100)
    print (secret)

    guess = int(raw_input("Ugibaj skrito številko: "))
    st_ugibanj = 0

    while st_ugibanj < 5:
        if guess != secret:
            print "Vaše ugibanje je bilo žal neuspešno. Skrita številka ni " + str(guess)
            guess = int(raw_input("Ugibaj še enkrat: "))
            st_ugibanj = st_ugibanj + 1
        elif guess == secret:
            print "Bravo, uganili ste!"
            break
if __name__ == '__main__':
    main()

