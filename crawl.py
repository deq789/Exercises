import requests
import re


def get_phones_from_text(text):
    """Return a list of numbers that follow format 8KKKNNNNNNN, extracted from given text"""
    pattern = r'[8]{1}[\s]?[(]?[\d+]{3}[)]? [\d+]{3}[-][\d+]{2}[\d+]?'
    numbers = re.findall(pattern, text)
    return numbers
