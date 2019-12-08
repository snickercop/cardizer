import xml.dom.minidom

def prettifyxml(xmlfile):
    f = open(xmlfile)
    string = f.read()
    f.close()

    string = xml.dom.minidom.parseString(string)
    pretty_string = string.toprettyxml()

    f = open(xmlfile, "w")
    f.write(pretty_string)
    f.close()

    return pretty_string
