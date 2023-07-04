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


def preprocess_code(text1):
	text1_new = []
	for i in range(len(text1)):
		text1[i] = text1[i].strip('\n')
		if "#" in text1[i]:
			if text1[i].find("#") != text1[i].split()[0]:
				text1[i] = text1[i][:text1[i].find("#")]
			else:
				text1[i] = ''
		if text1[i] != '':
			text1_new.append(text1[i].lower())
	return text1_new

def rename(text):
	dt_function = dict()
	dt_time = dict()
	t = 0
	for i in range(len(text)):
		if "def" in text[i]:
			dt_function[text[i].split()[1][:text[i].split()[1].find('(')]] = f"function{i}"
			a = text[i][text[i].find('(') + 1: -2].split(",")
			for j in range(len(a)):
				if a[j].find(":") != -1: a[j] = a[j][:a[j].find(":")]
				dt_time[a[j]] = f"times{t}"
				t += 1
	for i in range(len(text)):
		for k,v in dt_function.items():
			text[i] = text[i].replace(k,v)
		# for k,v in dt_time.items():
		# 	text[i] = text[i].replace(f" {k} ",v)
	return text

for i in rename(preprocess_code(read_files("new_haar.py","harmonic.py", True)[0])):
	print(i)
# print(rename(preprocess_code(read_files("new_haar.py","harmonic.py", True)[0])))
# print(type(preprocess_code(read_files("haar.py","harmonic.py", True)[0])))
# print("huy tablizahaar(n: int):".split()[1][:"huy tablizahaar(n: int):".split()[1].find("(")])
# a = "def function2(matrix1, matrix2):"["def function2(matrix1: list, matrix2: list):".find('(') + 1: -2].split(",")
# for i in range(len(a)):
# 	if a[i].find(":") != -1: a[i] = a[i][:a[i].find(":")]
# print(a)