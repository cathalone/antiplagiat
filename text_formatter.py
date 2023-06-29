def tabs_removing_for_line(line):
    words_w_spaces = line.split(" ")
    words = []
    for word in words_w_spaces:
        if word != "":
            words.append(word)
    result_line = words[0]
    for j in range(len(words) - 1):
        result_line = result_line + " " + words[j + 1]
    return result_line


def tabs_removing(text):
    lines = text.split("\n")
    result_text = tabs_removing_for_line(lines[0])
    for j in range(len(lines) - 1):
        result_text = result_text + "\n" + tabs_removing_for_line(lines[j + 1])
    return result_text


def empty_lines_removing(text):
    lines_w_empties = text.split("\n")
    lines = []
    for line in lines_w_empties:
        if line != "":
            lines.append(line)
    result_text = lines[0]
    for j in range(len(lines) - 1):
        result_text = result_text + "\n" + lines[j + 1]
    return result_text


def text_format(text):
    """ удаляет табы из начала каждой строки, удаляет пустые строки, удаляет лишние пробелы """
    return tabs_removing(empty_lines_removing(text))


def line_wrap(line, line_lenght):
    """ разбивает строку на несколько строк по заданной длине строки (нужно только для визуализации) """
    words = line.split(" ")
    lines = [words[0]]
    i = 1
    n = 0
    while i < len(words):
        if n == 0:
            while len(lines[n]) + 1 + len(words[i]) + 2 <= line_lenght:
                lines[n] = lines[n] + " " + words[i]
                if i + 1 == len(words):
                    break
                i += 1
        else:
            while len(lines[n]) + 1 + len(words[i]) + 5 <= line_lenght:
                lines[n] = lines[n] + " " + words[i]
                if i + 1 == len(words):
                    break
                i += 1
        lines[n] = lines[n] + " ▶"
        lines.append(words[i])
        i += 1
        n += 1
    lines = lines[:-1]
    lines[-1] = lines[-1].replace(" ▶", "")
    for i in range(len(lines)):
        if i != 0:
            lines[i] = " ▶ " + lines[i]
    result_text = lines[0]
    for i in range(len(lines) - 1):
        result_text = result_text + "\n" + lines[i + 1]
    return result_text



l = open('application.py').read()

txt = "ki eji fj ri ij rfi ej ki eji fj ri ij rfi ej ki eji fj ri ij rfi ej"

print(line_wrap(txt, 50))
