# Serial killer

***404 CTF WriteUp | Sécurité matérielle - Introduction***

## Énoncé

*Et votre prochaine épreuve est... le déménagement ? Vous avez donc invité votre amie haltérophile pour vous donner un coup de main et, en deux temps trois mouvements, tout est déballé et rangé. Tout se passait bien jusqu'au moment de rebrancher votre Arduino à votre PC. Elle essaie de rebrancher le port USB, mais ne dose pas sa force et... _CRAC !_ Le port se casse ! Cet événement vous affecte grandement.*

*Vous décidez de récupérer et de déchiffrer les dernières paroles que votre Arduino avait transmises à votre ordinateur afin de pouvoir les ajouter à son épitaphe.*

*`https://docs.arduino.cc/learn/communication/uart/#technical-specifications`*

Le fichier `chall.bin` nous est fourni *(dispo sur le git)*.

## Qu'est ce que c'est que ce fichier ? 

Bon, on va commencer par voir un peu ce que contient ce fichier : 

```bash
$ file chall.bin
chall.bin: data

$ strings chall.bin
T]S_S5
9_P|

$ xxd -b chall.bin
00000000: 00010110 11000001 10010001 01101101 10000111 00010101  ...m..
00000006: 11001100 01110110 11110101 01010101 00111011 11011001  .v.U;.
0000000c: 10010111 11010101 11011011 00100111 01010001 10110110  ...'Q.
00000012: 01010100 01011101 01010011 01011111 01010011 00110101  T]S_S5
00000018: 00011011 00111001 01011111 01010000 01111100 00011001  .9_P|.
0000001e: 01010101 01001001 11010111 11010101 01011111 00111001  UI.._9
00000024: 01011001 10010111 11010101 10001101 00010110 11001001  Y.....
0000002a: 11010111 01101101 10011001 01111101 01010001 10110011  .m.}Q.
00000030: 10111100 11101111 00000110 01011000 11010110 01100100  ...X.d
00000036: 11101111 00010111 01011001 10010101 11110111           ..Y..
```

Oui, des 0 et des 1 quoi... Rien de trop surprenant. D'après l'énoncé, il s'agirai d'un message provenant d'un arduino. Il s'agirai donc d'un message encodé avec le protocole UART. Je vous laisse revoir le lien de la documentation donné dans l'énoncé, tout y est expliqué clairement. 
Ce qui nous intéresse particulièrement est la partie *UART Messages*. Les 4 points clés à retenir sont : 
- Chaque bout de donnée est encapsulé par 2 bits : respectivement les bits *start* et *stop*
- Le bit *start* est tout le temps 0, le stop lui est toujours le même mais en fonction des systèmes, sa polarité peut varier.
- La partie des bits de données peut représenter à peu près n'importe quoi (simple caharactère, ou donnée), encodé en binaire.  
- En plus des 7 ou 8 bits généralement utilisés, la partie *data* contient probablement un bit de parité (pour chaque octet de données, la somme des 1 est paire, question d'intégrité pour la communication).

Le format du flag étant `404CTF{...}`, nous savons déjà qu'il y aura une redondance visible dès le début : la suite de bits permettant d'encoder le charactère `4`. Analysons donc le début du fichier et cherchons un pattern qui se répète, et qui ressemble à notre 4 en binaire : 

```bash
$ echo -n "404" | xxd -b
00000000: 00110100 00110000 00110100
# Ici, chaque charactère est encodé sur 8 bits, mais 7 suffisent pour la table ASCII

# première ligne en sortie de notre xxd 
# ce qui devrait être suffisant pour repérer la répétition
000101101100000110010001011011011000011100010101
# 1) le premier bit correspond au start, et vaut bien 0 
# 2) en prenant en compte au minimum les 9 autres bits suivants (au moins 7 pour un char. ASCII + 1 bit de partité + 1 bit stop), on recherche donc ce pattern :
0001011011 
# Bingo ! La même suite de bits est présente 10 bits plus loin, ce qui correspondrait à notre 2e '4', et ce qui nous confirmerai que chaque charactère est encodé sur 7 bits
0001011011 --> 0 0010110 1 1 # S DDDDDDD P E
# Nos 7 bits de données correspondent bien à un '4' en binaire (attention à l'endianness)
```

Voici donc notre format d'encodage : 
- Le bit *start* à 0, noté S
- 7 bits de données, notés D
- Le bit de parité, noté P 
- le bit *stop* à 1, noté E (pour *end*)

## Récupération du flag

 J'ai écris un petit script python qui va s'occuper de décoder en ASCII les 7 bits de chaque frame UART pour nous : 
 
```python
# Ce script corresponds au fichier script.py du repo
def binary_to_string(bits):
    return chr(int(bits[::-1], 2))

f = open("chall.bin", mode="rb")
data = f.read()

raw_binary = ""
for byte in data:
        # utile pour conserver les 0 non significatifs de début
        raw_binary += format(byte, '08b')
f.close()

frame_count = 0
while frame_count+10 <= len(raw_binary):
        frame = raw_binary[frame_count:frame_count+10]
        data_bits = frame[1:8]
        print(binary_to_string(data_bits), end="")
        frame_count += 10
```

Flag : `404CTF{Un3_7r1Ste_f1N_p0Ur_uN3_c4r73_1nn0c3nt3}`


