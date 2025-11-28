#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.
    
    Args:
        dictionary (dict): Python dictionary to serialize.
        filename (str): Output XML file name.
    """
    root = ET.Element("data")  # root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to string for XML

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file to a Python dictionary.
    
    Args:
        filename (str): Input XML file name.
    
    Returns:
        dict: Deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {child.tag: child.text for child in root}
        return result
    except Exception:
        return None
