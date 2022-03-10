import csv


def get_imc_tableau(file_path):
    file = open(file_path)
    csvreader = csv.reader(file)
    header = next(csvreader).pop().split(';')
    return header, [row.pop().split(';') for row in csvreader]