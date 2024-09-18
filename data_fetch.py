import csv
import json


def csv_to_json(csv_file, json_file):
    """
    Converts a CSV file to JSON format.

    Args:
        csv_file (str): Path to the CSV file.
        json_file (str): Path to the output JSON file.
    """

    with open(csv_file, 'r', encoding='utf-8') as csvfile, open(json_file, 'w', encoding='utf-8') as jsonfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    csv_file = 'dags/data/IMDB TMDB Movie Metadata Big Dataset (1M).csv'
    json_file = 'output.json'
    csv_to_json(csv_file, json_file)
