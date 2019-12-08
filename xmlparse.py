from card import Card, filize
from card import Card
import csv
import re
import sys

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
    tree = ET.parse(f)
    f.close()
    root = tree.getroot()
    for c in root:
        try:
            for element in c.findall('set'): #remove set tags from previous xml loads
                c.remove(element)
                print('found and removed set tag')
            cardtext = c.find('text').text
            card = Card(c.find('name').text,c.find('text').text)
            settag = ET.Element("set")
            settag.set('picURL', card.image)
            settag.text = set_code
            c.insert(1, settag)
            print(settag.attrib)
            print('inserted set tag')
            cards.append(card) # add card to cards list

        except AttributeError:
            print("card missing attributes")
            continue

    tree.write(xmlfile[:-4] + "-cardized.xml")
    return cards


    #for m in re.finditer(p, contents):



try:
    set = Set(sys.argv[1])
except:
    set = Set(input("Enter exact name of xml file, without extension: "))
try:
    set_code = sys.argv[2]
except:
    set_code = set.name[:3].upper()

cards = []
filename = f"{XML_PATH}{filize(set.name, 'xml')}"
cards = entriestocards(filename, cards)
#addimages(filename, cards)
