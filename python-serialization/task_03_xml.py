#!/usr/bin/python3
"""Module for serializing and deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to XML and saves it to a file"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserializes XML data from a file and returns a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
