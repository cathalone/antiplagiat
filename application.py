from PIL import Image, ImageFont, ImageDraw
import text_comparer as tc
import text_formatter as tf


def code_to_image(lines, line_number, percentage, n):
    img = Image.new('RGB', (1080, 720), 'black')
    img.save('pic/pic' + str(n) + '.jpg')
    img = Image.open('pic/pic' + str(n) + '.jpg')
    for i in range(len(lines)):
        line = tf.tabs_removing_for_line(lines[i])
        # line = tf.line_wrap(line, 30)
        # print(line)

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
        idraw = ImageDraw.Draw(img)
        idraw.text((60, 35 + i * 22), line, font=font, fill=(0, 255, 0))

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
        idraw = ImageDraw.Draw(img)
        idraw.text((0, 18 + i * 22), "_"*150, font=font, fill=(0, 255, 0))

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=9)
        idraw = ImageDraw.Draw(img)
        idraw.text((10, 38 + i * 22), "line " + str(line_number[i]+1), font=font, fill=(0, 255, 0))

        font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=9)
        idraw = ImageDraw.Draw(img)
        idraw.text((1050, 38 + i * 22), str(round(percentage[i]*100)) + " %", font=font, fill=(0, 255, 0))

    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
    idraw = ImageDraw.Draw(img)
    idraw.text((0, 18 + 30 * 22), "_" * 150, font=font, fill=(0, 255, 0))
    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=20)
    idraw = ImageDraw.Draw(img)
    idraw.text((5, 5), "FILE " + str(n), font=font, fill=(0, 255, 0))

    img.save('pic/pic' + str(n) + '.jpg')


def similar_strings(path1, path2, n):
    txcp = tc.TextComparer(path1, path2)
    lines = txcp.lines()
    l1 = lines[0]
    l2 = lines[1]
    misses = []
    for i in range(txcp.lenght()[0]):
        for j in range(txcp.lenght()[1]):
            if l1[i] != '' and l2[j] != '':
                misses.append((i, l1[i], j, l2[j], txcp.line_by_line_similitarity(i, j)))
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
    code_to_image(lines1, line_numbers1, percentage, 1)
    code_to_image(lines2, line_numbers2, percentage, 2)
    return sim


pics_gen('MongoDB.py', 'text_comparer.py')
