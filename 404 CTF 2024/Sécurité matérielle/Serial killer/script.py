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
