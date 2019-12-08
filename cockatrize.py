import os
import shutil
from datetime import date
import copy
from utility import prettifyxml

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

boilerplate = "cockatrized_boilerplate.xml"

mattributes = ['name', 'set', 'text']

def cockatrize(xmlfile):
    #prep output file
    data = open(xmlfile)

    #create source tree from input data
    intree = ET.parse(data)
    data.close()
    inroot = intree.getroot()

    #create output tree from boilerplate
    bp = open(boilerplate)
    outtree = ET.parse(bp)
    bp.close()
    outroot = outtree.getroot()


    setname = intree.find('record').find('set').text
    sets = outtree.find('sets') #find sets tags
    set = sets.find('set') #find set tag (sorry I didn't make the boilerplate)
    set.find('name').text = setname[:3].upper() #assign set code
    set.find('longname').text = setname
    set.find('settype').text = "Custom"
    set.find('releasedate').text = "2001-01-01"

    cards = outtree.find('cards') #find cards bin
    for incard in inroot:
        try:
            cardname = incard.find('name').text
            print(cardname)
            outcard = ET.SubElement(cards, "card")
            for tag in mattributes:
                print(tag)
                temp = ET.SubElement(outcard, tag)
                temp.text = incard.find(tag).text
                if tag == "set": #if this is a set tag
                    temp.set("picURL", cardname + ".png")
            ET.SubElement(outcard, "tablerow").text = "3"

        except AttributeError:
            print("card missing attribute")
            continue


    #finally, write the file...
    path = "01." + setname + "-cockatrized.xml"
    outtree.write(path)
    prettifyxml(path)

cockatrize(input("enter filename: "))
print("success!")
