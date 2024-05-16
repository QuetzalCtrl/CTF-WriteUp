secret_data = bytes.fromhex("68 5f 66 83 a4 87 f0 d1 b6 c1 bc c5 5c dd be bd 56 c9 54 c9 d4 a9 50 cf d0 a5 ce 4b c8 bd 44 bd aa d9")

flag = ""
for i in range(len(secret_data)):
	flag += chr(int((secret_data[i] + i)/2))
print(flag)