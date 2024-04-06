import xml.etree.ElementTree as ET

def parse_xml_et(fn):
    tree =  ET.parse(fn)
    root = tree.getroot()
    print('Doamins for: ' + root.attrib['name'])
    for child in root:
        print('\t' + child.attrib['name'], child.tag)

def add_xml_element(fn, el, attr, val):
    tree =  ET.parse(fn)
    root = tree.getroot()
    child = ET.Element(el)
    child.attrib[attr] = val
    root.append(child)
    tree.write(fn)

def change_xml_element(fn, el, attr, oldval, newval):
    tree =  ET.parse(fn)
    root = tree.getroot()
    child = root.find("./" + el + "[@" + attr + "='" + oldval + "']")
    child.attrib[attr] = newval
    tree.write(fn)

change_xml_element('./files_to_read/ef_author.xml', 'domain', 'name', 'Java', 'TypeScript')
add_xml_element('./files_to_read/ef_author.xml', 'domain', 'name', 'Java')
#parse_xml_et('./files_to_read/ef_author.xml')