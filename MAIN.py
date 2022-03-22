from PIL import Image, ImageDraw, ImageFont
import random

wordlist = open("WORDS/TOP_1000.txt", "r")
words = str.split(wordlist.read())

name = random.choice(words)

word = ""

for x in range(random.randint(4, 6)):
    word += random.choice(words) + " "

imglist = open("WORDS/IMGS.txt", "r")
imgs = str.split(imglist.read())

img = Image.open(random.choice(imgs))
width, height = img.size[:2]
new_width  = 1000
new_height = new_width * height / width
new_height = round(new_height)

img = img.resize((new_width, new_height), Image.ANTIALIAS)

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('Roboto-Bold.ttf', size=50)
(x, y) = (50, 50)
msg = "".join(word)
color = 'rgb(0, 0, 0)'

draw.text((x, y), msg, fill=color, font=font)

img.save("DONE/" + name + ".jpg")
