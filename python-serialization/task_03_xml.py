#!/usr/bin/python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):

    root = ET.Element("data")

    for key in dictionary:
        child = ET.Element(key)
        root.append(child)
        child.text = dictionary[key]

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
