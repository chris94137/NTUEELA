import numpy as np

# key should be a numpy array
def inv_key(key):
    det = int(round(np.linalg.det(key)))
    inv = np.linalg.inv(key)
    tem = (inv * det)
    modinv = np.mod(det ** 29, 31)
    return np.around(np.mod(tem * modinv, 31)).astype(int)
def char_to_int(txt):
	int_list = []
	for j in txt:
		for i in j:
			if i.isalpha():
				int_list.append(ord(i) - ord('A'))
			elif i == '_':
				int_list.append(26)
			elif i == '.':
				int_list.append(27)
			elif i == ',':
				int_list.append(28)
			elif i == '?':
				int_list.append(29)
			elif i == '!':
				int_list.append(30)
	return int_list
def int_to_char(int_txt):
	plain_str = ""
	for j in int_txt:
		for i in j:
			if i < 26:
				plain_str += chr(ord('A') + i)
			elif i == 26:
				plain_str += '_'
			elif i == 27:
				plain_str += '.'
			elif i == 28:
				plain_str += ','
			elif i == 29:
				plain_str += '?'
			elif i == 30:
				plain_str += '!'
	return plain_str


def main():
	file = open('b06901038.txt', 'r')
	print("b06901038")
	whole_file = file.readlines()
	first_cipher_txt = whole_file[0].split()
	first_public_key = whole_file[1].split()
	trash_line = whole_file[2].split()
	second_cipher_txt = whole_file[3].split()
	second_plain_txt = whole_file[4].split()
	the_other_cipher_txt = whole_file[5].split()
	
#Question 1
	first_cipher_int = char_to_int(first_cipher_txt)
	first_public_key = list(map(int, first_public_key))
	first_public_key_2d = []
	for i in [0, 3, 6]:
		first_public_key_2d.append(first_public_key[i + 0: i + 3])
	first_inverse_key = inv_key(first_public_key_2d)
	row_size = int(len(first_cipher_int) / 3)
	first_cipher_int = np.reshape(first_cipher_int, (3, row_size))
	first_plain_int = first_inverse_key.dot(first_cipher_int)
	first_plain_int = np.remainder(first_plain_int, 31)
	first_plain_txt = int_to_char(first_plain_int)
	print(first_plain_txt)

#Question 2
	second_plain_int = char_to_int(second_plain_txt)
	second_plain_int_2d = []
	for i in [0, 3, 6]:
		second_plain_int_2d.append(second_plain_int[i + 0: i + 3])
	second_plain_int_inverse = inv_key(second_plain_int_2d)
	plain_row_size = int(len(second_plain_int) / 3)
	second_plain_int = np.reshape(second_plain_int, (3, plain_row_size))
	second_cipher_int = char_to_int(second_cipher_txt)
	cipher_row_size = int(len(second_cipher_int) / 3)
	second_cipher_int = np.reshape(second_cipher_int, (3, cipher_row_size))
	second_public_key = second_cipher_int.dot(second_plain_int_inverse)
	second_public_key = np.remainder(second_public_key, 31)
	
	second_public_key_2d = second_public_key.tolist()
	for i in second_public_key_2d:
		for j in i:
			print(j, end = ' ')
	print('')
	second_public_key_inverse = inv_key(second_public_key_2d)
	the_other_cipher_int = char_to_int(the_other_cipher_txt)
	the_other_row_size = int(len(the_other_cipher_int) / 3)
	the_other_cipher_int = np.reshape(the_other_cipher_int, (3, the_other_row_size))
	the_other_plain_int = second_public_key_inverse.dot(the_other_cipher_int)
	the_other_plain_int = np.remainder(the_other_plain_int, 31)
	the_other_plain_txt = int_to_char(the_other_plain_int)
	print(the_other_plain_txt)
	

if __name__ == '__main__':
	main()
