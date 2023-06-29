def read_files(filename1, filename2, split):
	with open(filename1, encoding='utf-8') as f1, open(filename2, encoding='utf-8') as f2:
		if split:
			f1_data = f1.readlines()
			f2_data = f2.readlines()
		else:
			f1_data = f1.read()
			f2_data = f2.read()
		f1.close()
		f2.close()
		return f1_data, f2_data


def preprocess_code(text):
	for i in range(len(text)):
		text[i] = text[i].strip('\n')
	return text
