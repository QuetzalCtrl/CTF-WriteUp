#from flag import FLAG
import random as rd

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def f(a,b,n,x):
	return (a*x+b)%n

def encrypt(message,a,b,n):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f(a,b,n,x)
		encrypted += charset[x]

	return encrypted

n = len(charset)
a = rd.randint(2,n-1)
b = rd.randint(1,n-1)

# print(encrypt(FLAG,a,b,n))

# ENCRYPTED FLAG : -4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_


#### SOLUTION ####

# n est une constante, qui corresponds à la longueur de notre charset
# a et b sont bornés, et facilement bruteforce-able car peu de valeurs possibles (n valant 67)

encrypted = "-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_"
prefix = "404CTF{"

def find_a_b():
	for a in range(2,n-1):
		for b in range(1,n-1):
			if encrypt(prefix,a,b,n) == encrypted[:len(prefix)]:
				return a,b

# ETAPE 1 : bruteforcer les valeurs a et b grace a notre prefix de flag prévisible
a,b = find_a_b()

# ETAPE 2 : reconstruire le dictionnaire de chaque charactère avec son équivalent encrypté
# Puisqu'on a les bonnes valeurs de a, b et n, maintenant on peut encrypter tout correctement !
dict = {}
for char in charset:
	dict[encrypt(char, a, b, n)] = char

# ETAPE 3 : reconstituer le flag, en associant le charactère encrypté à son charactère en clair 
# dans les entrées de notre dictionnaire
flag = ""
for c in encrypted: 
	flag += dict[c]

print(flag)

# 404CTF{Th3_r3vEnGE_1S_c0minG_S0oN_4nD_w1Ll_b3_TErRiBl3_!}
