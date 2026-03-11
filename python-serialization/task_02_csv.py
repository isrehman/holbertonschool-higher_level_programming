#!/usr/bin/python3
"""Module for converting CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts CSV data to JSON format and writes to data.json"""
    try:
        with open(csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
