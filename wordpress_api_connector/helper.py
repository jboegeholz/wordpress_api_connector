import csv
import re


def clean_html(raw_html):
    clean_regex = re.compile('<.*?>')
    clean_text = re.sub(clean_regex, '', raw_html)
    return clean_text


def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as cf:
        writer = csv.writer(cf, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)