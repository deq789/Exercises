import requests
import re


def get_phones_from_url(url):
    """Return the list of phone numbers with format 8KKKNNNNNNN, in a given url"""
    r = requests.get(url)
    numbers = get_phones_from_text(r.text)
    numbers_set = set(numbers)  # remove duplicates
    return numbers_set


def get_phones_from_text(text):
    """Return a list of numbers that follow format 8KKKNNNNNNN, extracted from given text"""
    pattern = r'[8]{1}[\s]?[(]?[\d+]{3}[)]? [\d+]{3}[-][\d+]{2}[\d+]?'
    numbers = re.findall(pattern, text)
    return numbers