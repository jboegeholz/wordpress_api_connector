import csv


def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as cf:
        writer = csv.writer(cf, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)

