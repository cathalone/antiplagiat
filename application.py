from PIL import Image, ImageFont, ImageDraw


def text_to_image(text, n):
    img = Image.new('RGB', (1080, 720), 'black')
    img.save('pic/pic' + str(n) + '.jpg')
    img = Image.open('pic/pic' + str(n) + '.jpg')
    font = ImageFont.truetype("fonts/Hack-Regular.ttf", size=14)
    idraw = ImageDraw.Draw(img)
    idraw.text((8, 8), text, font=font, fill=(0,255,0))
    img.save('pic/pic' + str(n) + '.jpg')
    


stri = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkl\n" \
       "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkl\n" \
       "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkl"
text_to_image(stri, 1)