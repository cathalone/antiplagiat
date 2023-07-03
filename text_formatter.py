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


def line_wrap(text, line_length):
    if len(text) > line_length:
        words = text.split()
        formatted_text = ''
        current_line_length = 0

        for word in words:
            word_length = len(word)

            if current_line_length + 1 + word_length + 5 <= line_length:
                formatted_text += word + ' '
                current_line_length += word_length + 1
            else:
                formatted_text += '\n' + word + ' '
                current_line_length = word_length + 1

        formatted_text = formatted_text.strip()

        lines = formatted_text.split("\n")
        for i in range(len(lines)):
            if i == 0:
                length = line_length - len(lines[i]) + 3
                lines[i] = lines[i] + " " * length + "▶"
            elif i == len(lines) - 1:
                lines[i] = " ▶ " + lines[i]
            else:
                length = line_length - len(lines[i])
                lines[i] = " ▶ " + lines[i] + " " * length + "▶"

        result_text = lines[0]
        for i in range(len(lines) - 1):
            result_text = result_text + "\n" + lines[i + 1]

        return result_text
    else:
        return text
