from PIL import Image, ImageFont, ImageDraw
import text_comparer as tc
import text_formatter as tf


def code_to_image(lines1, line_number1, percentage1, lines2, line_number2):
    img = Image.new('RGB', (1080, 720), 'black')
    img.save('pic/pic1.jpg')
    img = Image.open('pic/pic1.jpg')
    n1 = 0
    for i in range(len(lines1)):
        line1 = tf.tabs_removing_for_line(lines1[i])
        line1 = tf.line_wrap(line1, 50)

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
        idraw = ImageDraw.Draw(img)
        idraw.text((60, 35 + i * 22 + n1 * 18), line1, font=font, fill=(0, 255, 0))

        line = tf.tabs_removing_for_line(lines2[i])
        line = tf.line_wrap(line, 50)

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
        idraw = ImageDraw.Draw(img)
        idraw.text((520 + 60, 35 + i * 22 + n1 * 18), line, font=font, fill=(0, 255, 0))

        n1 += max(len(line.strip().split('\n')) - 1, len(line1.strip().split('\n')) - 1)

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
        idraw = ImageDraw.Draw(img)
        idraw.text((0, 18 + 22 + i * 22 + n1 * 18), "_" * 150, font=font, fill=(0, 255, 0))

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=9)
        idraw = ImageDraw.Draw(img)
        idraw.text((10, 38 + i * 22 + n1 * 18), "line " + str(line_number1[i] + 1), font=font, fill=(0, 255, 0))

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=9)
        idraw = ImageDraw.Draw(img)
        idraw.text((1050, 38 + i * 22 + n1 * 18), str(round(percentage1[i] * 100)) + " %", font=font, fill=(0, 255, 0))

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
        idraw = ImageDraw.Draw(img)
        idraw.text((0, 18 + 22 + i * 22 + n1 * 18), "_" * 150, font=font, fill=(0, 255, 0))

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=9)
        idraw = ImageDraw.Draw(img)
        idraw.text((520 + 10, 38 + i * 22 + n1 * 18), "line " + str(line_number2[i] + 1), font=font, fill=(0, 255, 0))

    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
    idraw = ImageDraw.Draw(img)
    idraw.text((0, 18), "_" * 150, font=font, fill=(0, 255, 0))
    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=20)
    idraw = ImageDraw.Draw(img)
    idraw.text((5, 5), "FILE 1", font=font, fill=(0, 255, 0))

    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=20)
    idraw = ImageDraw.Draw(img)
    idraw.text((520 + 5, 5), "FILE 2", font=font, fill=(0, 255, 0))

    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=20)
    idraw = ImageDraw.Draw(img)
    idraw.text((515, 0), "|\n" * 150, font=font, fill=(0, 255, 0))

    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=20)
    idraw = ImageDraw.Draw(img)
    idraw.text((1035, 0), "|\n" * 150, font=font, fill=(0, 255, 0))

    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=30)
    idraw = ImageDraw.Draw(img)
    idraw.text((1055, 0), "%", font=font, fill=(0, 255, 0))

    img.save('pic/pic1.jpg')


def similar_strings(path1, path2, n):
    txcp = tc.TextComparer(path1, path2)
    lines = txcp.lines()
    l1 = lines[0]
    l2 = lines[1]
    misses = []
    for i in range(txcp.length()[0]):
        for j in range(txcp.length()[1]):
            if l1[i] != '' and l2[j] != '':
                if 'import' in l1[i]:
                    misses.append((i, l1[i], j, l2[j], txcp.line_by_line_similarity(i, j) - 1))
                else:
                    misses.append((i, l1[i], j, l2[j], txcp.line_by_line_similarity(i, j)))
    misses.sort(key=lambda obj: obj[4])
    return misses[-1:-n - 1:-1]


def pics_gen(path1, path2):
    misses = similar_strings(path1, path2, 30)
    lines1 = []
    lines2 = []
    line_numbers1 = []
    line_numbers2 = []
    percentage = []
    for line in misses:
        lines1.append(line[1])
        lines2.append(line[3])
        line_numbers1.append(line[0])
        line_numbers2.append(line[2])
        percentage.append(line[4])
    txcp = tc.TextComparer(path1, path2)
    sim = txcp.similarity()
    code_to_image(lines1, line_numbers1, percentage, lines2, line_numbers2)
    return sim


if __name__ == '__main__':
    print(pics_gen('test1.py', 'test2.py'))
