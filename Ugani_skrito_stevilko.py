# -*- coding: utf-8 -*-

import random

secret = random.randint(1,100)

guess = int(raw_input("Ugani skrito številko: "))

if secret == guess:
    print"Res je, skrita številka je %s! Čestitamo!:)" % secret
else:
    print "Vaše ugibanje je bilo žal neuspešno. Poizkusite znova"


#prava številka
print secret
