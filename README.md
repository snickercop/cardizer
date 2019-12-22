# Cardizer

Cardizer is a collection of python scripts for converting spreadsheets of card name/rulestext data into images, for prototyping in tabletop simulators such as cockatrice.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You'll need PIL to run most of this. 

```
pip install pil
```

Compatability with Pillow hasn't been tested yet, but try changing the import statement in card.py and give it a shot!


### XML Input Format

This script is ideal for converting spreadsheets of information into card-sized images with text on them. You can use XML data if you have it already, but if you don't, follow <a href="https://www.excel-easy.com/examples/xml.html">this tutorial</a>. (Haven't tried with Google Sheets or OpenOffice yet, but there should be a way...)

It doesn't matter what your xml looks like, as long as it conforms to the following criteria.
1. The root tag has elements containing card data as direct children--one element per card (note that it doesn't matter what the tag is actually called)
2. The card carrying elements each have one ```name``` element and one ```text``` element

The following is an example of valid cardizer input xml:
```
<card-data>
	<record>
		<name>Bear</name>
		<text>Creature, 2 mana, 2/2</text>
    <artist>John Doe</artist>
	</record>
	<record>
		<name>Orc</name>
		<text>Creature, 3 mana, 2/2</text>
    <artist>Jane Doe</artist>
	</record>
</card-data>
```

Note that the presence of the ```artist``` tag is not a problem--the system will just skip over it. 

### Execution

To make your cards (images), simply run ```python xmlparse.py [name of xml file]```. A feature to make cards automatically go to a destination folder is in the works, but in the meantime you can either A) figure it out yourself or B) suffer from extreme folder clutter.

### Cockatrizer Script

To reformat your xml for use in Cockatrice, run ```python cockatrize.py``` and enter the filename of the xml output by xmlparser (should be called ```[name of original xml file]-cardized.xml```). Put the resulting xml in the custom sets folder, move your images to the custom images folder (both can be accessed in the "Card Database" dropdown), and restart Cockatrice. 

