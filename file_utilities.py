import autopep8 as ap


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


def delete_comments(text1):
    text1 = text1.split('\n')
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
    return '\n'.join(text1_new)


def preprocess_code(text):
    text = delete_comments(text)
    text = ap.fix_code(text.lower())
    return text


