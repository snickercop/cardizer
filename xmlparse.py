from card import Card, filize
from card import Card
import csv
import re

SET_CODE = 'SHO'

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

XML_PATH = r'' # set to desired drop-in location of XML file
              # in Cockatrice this will be the "custom sets" folder
class Set:
    def __init__(self, name):
        self.name = name
        self.cards = []

def entriestocards(xmlfile, cards):
    f = open(xmlfile)
    settag = ET.Element("set")
    tree = ET.parse(f)
    f.close()
    root = tree.getroot()
    for c in root:
        try:
            for element in c.findall('set'): #remove set tags from previous xml loads
                c.remove(element)
                print('found and removed set')

            card = Card(c.find('name').text,c.find('text').text)
            settag.set('picURL', card.image)
            settag.text = SET_CODE
            c.insert(1, settag)
            print('inserted set tag')
            cards.append(card) # add card to cards list

        except AttributeError:
            print("card missing attributes")
            continue

    tree.write(xmlfile)
    return cards


    #for m in re.finditer(p, contents):



set = Set("shonen showdown")
cards = []
filename = f"{XML_PATH}{filize(set.name, 'xml')}"
cards = entriestocards(filename, cards)
#addimages(filename, cards)
