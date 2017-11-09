import xmltodict

def processXML(FILE):
    with open(FILE) as XML_FILE:
        filecontent = XML_FILE.read()
        XML_DICT = xmltodict.parse(filecontent)
        return XML_DICT