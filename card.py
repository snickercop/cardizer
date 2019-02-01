from PIL import Image, ImageDraw, ImageFont

TITLE_FONT_SIZE = 35
RULES_FONT_SIZE = 18

titleF = ImageFont.truetype('fonts/roboto/Roboto-Black.ttf', TITLE_FONT_SIZE)
rulesF = ImageFont.truetype('fonts/roboto/Roboto-Black.ttf', RULES_FONT_SIZE)

def makeCardImage(name, rules):
    img = Image.new('RGB', (500, 726), color = 'white')

    d = ImageDraw.Draw(img)
    d.text((20,20), name, fill=(0,0,0), font=titleF)
    d.text((20,500), rules, fill=(0,0,0), font=rulesF)

    file = name + '.png'
    img.save(file)

    return file

class Card:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
        self.image = makeCardImage(name, rules)

# example card for testing
c = Card("example card", "example rules")
