from PIL import Image, ImageFont, ImageDraw
import text_comparer as tc
import difflib


def text_to_image(text, n):
    img = Image.new('RGB', (1080, 720), 'black')
    img.save('pic/pic' + str(n) + '.jpg')
    img = Image.open('pic/pic' + str(n) + '.jpg')
    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
    idraw = ImageDraw.Draw(img)
    idraw.text((8, 8), text, font=font, fill=(0,255,0))
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
    return misses[-1:-n-1:-1]

def pics_gen(path1, path2):
    misses = similar_strings(path1, path2, 30)
    im1txt = ''
    im2txt = ''
    for line in misses:
        im1txt = im1txt + 'line' + str(line[0]) + ':  ' + line[1] + '\n'
        im2txt = im2txt + 'line' + str(line[2]) + ':  ' + line[3] + '\n'
    text_to_image(im1txt, 1)
    text_to_image(im2txt, 2)


pics_gen('application.py', 'text_comparer.py')